from django.contrib import admin
from .models import Category, Book, User, IssuedBook

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(IssuedBook)