from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.timezone import datetime
from django import forms

class Category(models.Model):
    uname = models.CharField(max_length=100, default="default_category")

    def __str__(self):
        return self.uname

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField()
    copies_available = models.IntegerField(default=0)  

    def __str__(self):
        return self.title


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='library_user_set',  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='library_user_permissions_set',  # Custom related name
        blank=True
    )
    password = models.CharField(max_length=128, null=True, blank=True) 
    def __str__(self):
        return self.username

class IssuedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        user_display = self.user.username if self.user else "Anonymous"
        return f"{user_display} issued {self.book.title}"
