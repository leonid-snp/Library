from django.contrib import admin

from library.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'date_birth', 'date_death')
    list_filter = ('date_birth', 'date_death')
    search_fields = ('last_name', 'first_name')
