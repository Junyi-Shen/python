from django.shortcuts import render
from .models import Book, Author, Book_Instance

# Create your views here.

def home(request):
    contents = {'books': Book.objects.all()}
    return render(request, 'mylibraray/index.html', contents)

def author(request):
    contents = {'authors': Author.objects.all()}
    return render(request, 'mylibraray/author_list.html', contents)

def getBook(request, received_id):
    book = Book.objects.get(id = received_id)
    book_instance = Book_Instance.objects.get(book_id = received_id)
    contents = {'book': book, 'book_instance': book_instance}
    return render(request, 'mylibraray/bookInstance.html', contents)