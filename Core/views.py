from django.shortcuts import render, get_object_or_404

from Books.models import Book, Category
# Create your views here.

def home(request, slug=None):
    books = Book.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', {'books':books, 'categories': category })

def categoryFilter(request, category=None):
    category_instance = get_object_or_404(Category, category=category)
    books = Book.objects.filter(category=category_instance)
    categories = Category.objects.all()
    return render(request, 'home.html', {'books': books, 'categories': categories})

