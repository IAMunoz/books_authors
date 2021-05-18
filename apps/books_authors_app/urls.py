from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('book', views.book),
    path('authors', views.authors),
    path('author', views.author),
    path('authors/<int:number>', views.autor),
    path('books/<int:number>', views.libro),
]