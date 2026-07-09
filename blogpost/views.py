from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost , Comment

def HomePage(request):
    Posts = BlogPost.objects.all().order_by("-likes")
    context = {"posts" : Posts}
    return render(request , "home/index.html" , context)




def DetailPage(request , pk):
    post = get_object_or_404(BlogPost , pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email" , None)
        address = request.POST.get("address" , "")
        city = request.POST.get("city" , "")
        province = request.POST.get("state" , "")
        hide_name = request.POST.get("hide_name" , "")
        hide_name = True if hide_name else False
        comment = request.POST.get("comment")

        Comment.objects.create(
            nickname=name,
            email=email,
            address=address,
            city=city,
            province=province,
            hide_name=hide_name,
            comment=comment,
            post=post
        )
    context = {'post': post , "comments" : comments}
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

