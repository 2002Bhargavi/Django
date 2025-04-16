from django.shortcuts import render, redirect
from .models import Category, Book, IssuedBook,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def books_in_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        books = Book.objects.filter(category=category)
        return render(request, 'books_in_category.html', {'category': category, 'books': books})
    except Category.DoesNotExist:
        messages.error(request, "Category not found.")
        return redirect('category_list')

def issue_book(request, book_id):
    import pdb;pdb.set_trace()
    try:
        book = Book.objects.get(id=book_id)
        if book.copies_available > 0:
            user=IssuedBook.objects.create(user=request.user, book=book) if request.user.is_authenticated else IssuedBook.objects.create(book=book)
            # IssuedBook.objects.create(user=user, book=book)
            book.copies_available -= 1
            book.save()
            messages.success(request, f"You have issued '{book.title}' successfully.")
        else:
            messages.error(request, "No copies available to issue this book.")
    except Book.DoesNotExist:
        messages.error(request, "Book not found.")
    return redirect('books_in_category', category_id=book.category.id if 'book' in locals() else None)


def add_book(request):
    if request.method == 'POST':  
        form = BookForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('books_list')  
    else: 
        form = BookForm()  
    
    return render(request, 'add_book.html', {'form': form})  


def books_list(request):
    books = Book.objects.all()  
    return render(request, 'books_list.html', {'books': books})