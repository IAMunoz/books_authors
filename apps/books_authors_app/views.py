from django.shortcuts import redirect, render
from .models import Books, Authors

def index(request):
    books = Books.objects.all().order_by('id')
    context = {
        'books' : books
    }
    return render(request, 'index.html', context)

def book(request):
    Books.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')
def authors(request):
    authors = Authors.objects.all().order_by('id')
    context = {
        'authors': authors
    }
    return render( request, 'authors.html', context)

def author(request):
    Authors.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notas = request.POST['notes']
    )
    return redirect('/authors')

def autor(request, number):
    if request.method == 'GET':
        autor = Authors.objects.get(id=number)
        libros = autor.books.all()
        libroAll = Books.objects.exclude(Authors__id=number).order_by('title')
        context = {
            'autor' : autor,
            'libros' : libros,
            'libroAll' : libroAll
        }
        return render(request, 'autor.html', context)
    else:
        autor = Authors.objects.get(id=number)
        libroAdd = Books.objects.get(id = int(request.POST['libro']))
        autor.books.add(libroAdd)
        return redirect(f'/authors/{autor.id}')

def libro(request, number):
    if request.method == 'GET':
        libro = Books.objects.get(id=number)
        autores = libro.Authors.all()
        autorAll = Authors.objects.exclude(books__id=number).order_by('last_name')
        context = {
            'libro' : libro,
            'autores' : autores,
            'autorAll' : autorAll
        }
        return render(request, 'libro.html', context)
    else:
        libro = Books.objects.get(id=number)
        autorAdd = Authors.objects.get(id = int(request.POST['author']))
        libro.Authors.add(autorAdd)
        return redirect(f'/books/{libro.id}')
        
   