from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    checked_out = models.BooleanField(default=False, verbose_name='Взято на читання')
    due_date = models.DateField(null=True, blank=True, verbose_name='Термін повернення')
    borrower = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Позичальник')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


