from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

def proba_pera(request):
    res = '<h1>'
    for each in request.session.keys():
        res += str(each)
        res += '<br>'
    res += '</h1>'
    res += request.session['_auth_user_id'] + '<br>' + request.session['_auth_user_backend'] + '<br>' + request.session['_auth_user_hash']
    res = request.session.get('zalupa_konskaya', 'zal')
    return HttpResponse(res)