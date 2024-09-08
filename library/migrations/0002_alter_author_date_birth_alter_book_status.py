# Generated by Django 4.2 on 2024-09-08 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateField(default=django.utils.timezone.localdate, help_text='Укажите дату рождения автора', verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Issued', 'Выдана'), ('In_stock', 'В наличии')], default=('In_stock', 'В наличии'), help_text='Укажите статус книги', verbose_name='Статус книги'),
        ),
    ]
