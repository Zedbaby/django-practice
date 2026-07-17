from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required 
from .models import BlogPost , Comment
from .forms import BlogPostCommentForm
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .decorators import post_owner_required


def HomePage(request):
    Posts_list = BlogPost.objects.all()
    # paginator for posts
    paginator = Paginator(Posts_list , 4)
    page = request.GET.get("page")
    try:
        Posts = paginator.page(page)
    except PageNotAnInteger:
        Posts = paginator.page(1) 
    except EmptyPage:
        Posts = paginator.page(paginator.num_pages)


    context = {"posts" : Posts}
    return render(request , "home/index.html" , context)

def DetailPage(request , pk):
    post = get_object_or_404(BlogPost , pk=pk)
    comments_list = Comment.objects.filter(post=post , state=Comment.STATE_CHOICES_APPROVED)
    # paginator for comments
    paginator = Paginator(comments_list , 4)
    page = request.GET.get("page")
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1) 
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    # comments posts
    form = BlogPostCommentForm()
    if request.method == "POST":
        if "nickname" in request.POST:
            form = BlogPostCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                form = BlogPostCommentForm()
        else:
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
        



    context = {'post': post , "comments" : comments , "form" : form}
    return render(request , "detail/detail.html" , context)


def test_func(user , *args , **kwargs ):
    pk = kwargs.get('pk')
    post = get_object_or_404(BlogPost , pk=pk)
    return user == post.author
@post_owner_required
def DeletePost(request, pk):
    post = get_object_or_404(BlogPost , pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blogpost:home")
    context = {"post" : post}
    return render(request , "detail/delete.html" , context)


@post_owner_required
def UpdatePost(request , pk):
    post = get_object_or_404(BlogPost , pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        picture = request.FILES.get("picture")
        post.title = title
        post.description = description
        post.picture = picture
        post.save()
        return redirect("blogpost:home")

    context = {"post" : post}
    return render(request , "detail/update.html" , context)
    
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
        picture = request.FILES.get("picture")
        author = request.user

        newpost = BlogPost.objects.create(
            title=name ,
            description=description ,
            author=author ,
            picture = picture
        )
        newpost.save()
        return redirect("blogpost:home")
    return render(request , "add/add.html")

