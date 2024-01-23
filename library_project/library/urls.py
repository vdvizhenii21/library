from django.conf.urls import include, url
from .views import OverdueBooksListView, BookListView

urlpatterns = [
    url('overdue-books/', OverdueBooksListView.as_view(), name='overdue_books'),
    url('books/', BookListView.as_view(), name='book_list'),

]
