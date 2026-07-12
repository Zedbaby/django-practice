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
    STATE_CHOICES_APPROVED = "a"
    STATE_CHOICES_REJECTED = "r"
    STATE_CHOICES_PERDING = "p"
    STATE_CHOICES = (
        (STATE_CHOICES_APPROVED ,"تایید شده"),
        (STATE_CHOICES_REJECTED ,"رد شده"),
        (STATE_CHOICES_PERDING ,"در حال بررسی"),
    )

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
    # برای تایید کردن نظرات که ایا قابل نمایش هست یا خیر
    state = models.CharField(max_length=1 , default=STATE_CHOICES_PERDING , verbose_name="وضعیت کامنت" , choices=STATE_CHOICES)