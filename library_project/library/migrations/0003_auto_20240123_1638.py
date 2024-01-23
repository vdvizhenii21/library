# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20240123_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(verbose_name='Автор', to='library.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(verbose_name='Позичальник', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='checked_out',
            field=models.BooleanField(verbose_name='Взято на читання', default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='due_date',
            field=models.DateField(verbose_name='Термін повернення', blank=True, null=True),
        ),
    ]
