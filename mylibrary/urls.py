
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('book_detail/', views.book_detail, name='library-bookDetail'),
    path('author_details/', views.author_details, name='library-authorDetails'),
        
]
