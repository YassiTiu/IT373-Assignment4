from django.shortcuts import render
from .models import Book, Category, Author

def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    
    context = {
        'books': books,
        'categories': categories,
        'authors': authors,
        'total_books': books.count(),
        'total_categories': categories.count(),
        'total_authors': authors.count(),
    }
    return render(request, 'mainapp/home.html', context)


def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'mainapp/books_list.html', context)


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'mainapp/categories_list.html', context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'mainapp/book_detail.html', context)


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    books = category.books.all()
    context = {'category': category, 'books': books}
    return render(request, 'mainapp/category_detail.html', context)
