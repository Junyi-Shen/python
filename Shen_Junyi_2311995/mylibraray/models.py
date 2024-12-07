from django.db import models

# Create your models here.

class Author(models.Model):
    fName = models.CharField(max_length = 200)
    lName = models.CharField(max_length = 200)
    dob = models.DateField()

    def __str__(self):
        return f"{self.fName}, {self.lName}" 

class Genre(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length = 13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
    def GetId(self):
        return self.id

class Book_Instance(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    status = models.CharField(max_length = 1)
    dueDate = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.book.title