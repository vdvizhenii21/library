from django.shortcuts import render
from django.db.models import Q
from django.views.generic import View
from .models import Book
from .forms import SearchForm


class BookListView(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        search_term = request.GET.get('search_term', '')
        form = SearchForm(initial={'search_term': search_term})

        if search_term:
            books = books.filter(Q(title__icontains=search_term) | Q(author__name__icontains=search_term))
        return render(request, self.template_name, {'books': books, 'form': form})


def overdue_books(request):

    books = Book.objects.filter(checked_out=True)

    context = {
        'books': books,
    }
    return render(request, 'overdue_books.html', context)
