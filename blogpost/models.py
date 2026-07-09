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
    nickname = models.CharField(max_length=255)
    email = models.EmailField(null=True , blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=255 , blank=True)
    province = models.CharField(max_length=255 , choices=PROVINCE_CHOICES , blank=True)
    hide_name = models.BooleanField(default=True)
    comment = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(to=BlogPost , on_delete=models.CASCADE)