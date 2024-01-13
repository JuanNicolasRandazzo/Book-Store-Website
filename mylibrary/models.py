from django.db import models

# Create your models here.

class Author(models.Model):

    ### Author caption is the last name, first name
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    dob = models.DateField()

    def __str__(self):

        return f"{self.first_name}, {self.last_name}"



class Genre(models.Model):

    name = models.CharField(max_length=200)
    def __str__(self):

        return self.name

class Book(models.Model):

    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Book_Instance(models.Model):

    book_status_options= [('booked', 'Booked'),('available', 'Available'),('reserved', 'Reserved'),]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length = 30, choices= book_status_options)
    due_date = models.DateField()

    def __str__(self):
        return self.book
    

    
