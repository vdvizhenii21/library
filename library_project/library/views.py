from django.shortcuts import render
from datetime import date
from django.db.models import Q
from django.views.generic import View, ListView
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


class OverdueBooksListView(ListView):
    model = Book
    template_name = 'overdue_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(checked_out=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context
