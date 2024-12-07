from django.contrib import admin
from .models import Author, Genre, Book, Book_Instance

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Book_Instance)