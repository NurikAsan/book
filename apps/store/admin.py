from django.contrib import admin

from apps.store.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
