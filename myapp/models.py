from django.db import models
from django.contrib.auth.models import User

# Create your models here.



from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)  # عنوان خبر
    content = models.TextField()  # محتوای خبر
    author = models.CharField(max_length=100)  # نویسنده
    date_published = models.DateTimeField(auto_now_add=True)  # تاریخ انتشار
    # اختیاری: تصویر شاخص برای خبر (اگر نیاز دارید)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title





class Message(models.Model):
    name = models.CharField(max_length=100)  # نام کاربر
    email = models.EmailField()  # ایمیل کاربر
    subject = models.CharField(max_length=200)  # موضوع پیام
    message = models.TextField()  # محتوای پیام
    date_received = models.DateTimeField(auto_now_add=True)  # تاریخ ارسال پیام

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"




class ContactUs(models.Model):
      message = models.TextField()
      name = models.CharField(max_length=255)  # نام کاربر
      email = models.EmailField()  # ایمیل کاربر

      def __str__(self):
          return self.name





class NewsDatabase(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publisher = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)


    def __str__(self):
        return self.title











