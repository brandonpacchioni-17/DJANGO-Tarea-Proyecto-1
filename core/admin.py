from django.contrib import admin
from django.contrib import admin
from .models import Author, Book, Loan
from .models import Book, Author, Loan, Review

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Review)

