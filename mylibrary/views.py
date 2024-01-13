from django.shortcuts import render
from .models import Author,Genre,Book,Book_Instance

# Create your views here.




def home(request):

    return render(request, 'mylibrary/index.html',{'books':Book.objects.all(), 'title': 'Home Page'})

def book_detail(request):
    
    return render(request, 'mylibrary/bookInstance.html',{'bDetail':Book_Instance.objects.all(), 'title': 'Book Details'})

def author_details(request):

    return render(request, 'mylibrary/author_list.html',{'aDetails':Author.objects.all(), 'title': 'Author Details'})
