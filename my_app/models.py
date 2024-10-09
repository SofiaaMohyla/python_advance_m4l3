from django.db import models
from django.contrib.auth.models import User, AbstractUser  # Вбудована модель користувачів Django

from django.conf import settings



# Модель автора
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я автора")
    biography = models.TextField(blank=True, verbose_name="Біографія")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")

    def __str__(self):
        return self.name


# Модель жанру
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")
    description = models.TextField(blank=True, verbose_name="Опис жанру")

    def __str__(self):
        return self.name


# Модель книги
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва книги")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    publication_date = models.DateField(verbose_name="Дата публікації")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    genre = models.ManyToManyField(Genre, related_name='books', verbose_name="Жанри")
    available_copies = models.IntegerField(default=1, verbose_name="Доступні примірники")

    def __str__(self):
        return self.title


# Модель оренди книги
class Borrow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrows', verbose_name="Користувач")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows', verbose_name="Книга")
    borrow_date = models.DateField(auto_now_add=True, verbose_name="Дата оренди")
    return_date = models.DateField(null=True, blank=True, verbose_name="Дата повернення")
    is_returned = models.BooleanField(default=False, verbose_name="Повернено")

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
