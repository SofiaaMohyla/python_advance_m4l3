from django.shortcuts import render, get_object_or_404, redirect

from my_app.models import Author, Genre, Book, Borrow


# Create your views here.
def index(request):
    context = {
        "render_string": "Hello, world!"
    }
    return render(request, "index.html", context)

def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author_list.html', context)


# Список жанрів та форма для додавання нового жанру
def genre_list(request):
    genres = Genre.objects.all()

    # Якщо запит POST, обробляємо дані форми
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Додаємо новий жанр, якщо поля не порожні
        if name:
            Genre.objects.create(name=name, description=description)
            return redirect('genre_list')  # Переходимо на ту ж саму сторінку після додавання

    context = {
        'genres': genres
    }
    return render(request, 'genre_list.html', context)

# Список книг
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book_list.html', context)


# Інформація про оренди
def borrow_list(request):
    borrows = Borrow.objects.all()
    context = {
        'borrows': borrows
    }
    return render(request, 'borrow_list.html', context)


# Деталі конкретної книги
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)