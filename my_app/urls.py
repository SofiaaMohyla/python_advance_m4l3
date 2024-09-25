from django.urls import path
from my_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path('authors/', views.author_list, name='author_list'),
    path('genres/', views.genre_list, name='genre_list'),
    path('books/', views.book_list, name='book_list'),
    path('borrows/', views.borrow_list, name='borrow_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
