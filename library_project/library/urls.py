from django.conf.urls import include, url
from .views import overdue_books, BookListView

urlpatterns = [
    url('overdue-books/', overdue_books, name='overdue_books'),
    url('books/', BookListView.as_view(), name='book_list'),

]
