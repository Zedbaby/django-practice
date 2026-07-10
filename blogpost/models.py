from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.title}"


class Comment(models.Model):
    PROVINCE_CHOICES = (
        ("kh razavi","خراسان رضوی"),
        ("Tehran","تهران"),
        ("Esfehan","اصفهان"),
    )
    nickname = models.CharField(max_length=255, verbose_name="نام کاربری")
    email = models.EmailField(null=True , blank=True, verbose_name="ایمیل")
    address = models.TextField(blank=True, verbose_name="آدرس")
    city = models.CharField(max_length=255 , blank=True, verbose_name="شهر")
    province = models.CharField(max_length=255 , choices=PROVINCE_CHOICES , blank=True, verbose_name="استان")
    hide_name = models.BooleanField(default=True, verbose_name="نمایش نام کاربری")
    comment = models.TextField(verbose_name="نظر")
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name="زمان ویرایش")
    post = models.ForeignKey(to=BlogPost , on_delete=models.CASCADE, verbose_name="پست مربوطه")