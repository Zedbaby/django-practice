from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost , Comment
from .forms import BlogPostCommentForm

def HomePage(request):
    Posts = BlogPost.objects.all().order_by("-likes")
    context = {"posts" : Posts}
    return render(request , "home/index.html" , context)




def DetailPage(request , pk):
    post = get_object_or_404(BlogPost , pk=pk)
    comments = Comment.objects.filter(post=post)

    form = BlogPostCommentForm()
    if request.method == "POST":
        form = BlogPostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = BlogPostCommentForm()
    context = {'post': post , "comments" : comments , "form" : form}
    return render(request , "detail/detail.html" , context)

def RecentPost(request):
    post = BlogPost.objects.all().order_by("-datetime_created")[:5]
    context = {"posts":post}
    return render(request , "home/index.html" , context)


# این دکورتور برای وقتیه که کاربر لاگین نکرده 
# و میخواد از یکی از امکانات سایت (اضافه کردن پست) استفاده کنه 
@login_required
def AddPost(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        author = request.user

        BlogPost.objects.create(
            title=name ,
            description=description ,
            author=author ,
        )
        BlogPost.save()


    return render(request , "add/add.html")

