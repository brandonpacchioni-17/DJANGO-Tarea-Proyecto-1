from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"

        
    