from django.urls import path
from .views import category_list, books_in_category, issue_book
from library import views

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', books_in_category, name='books_in_category'),
    path('issue/<int:book_id>/', issue_book, name='issue_book'),
    path('add_book/',views.add_book,name='add_book'),
    path('books_list/',views.books_list,name='books_list'),
]