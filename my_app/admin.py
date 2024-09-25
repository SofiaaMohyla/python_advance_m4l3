from django.contrib import admin

from my_app.models import Author, Genre, Book, Borrow

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Borrow)