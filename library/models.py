from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    """
    Model representing a book in the library.
    """
    title = models.CharField(max_length=255, help_text="Title of the book")
    author = models.CharField(max_length=255, help_text="Author of the book")
    isbn = models.CharField(max_length=13, unique=True, help_text="Unique ISBN number for the book")
    published_date = models.DateField(help_text="Publication date of the book")
    copies_available = models.PositiveIntegerField(help_text="Number of available copies")

    def __str__(self):
        return self.title


class Transaction(models.Model):
    """
    Model representing a book lending transaction for a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who borrowed the book")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book that was borrowed")
    checkout_date = models.DateTimeField(auto_now_add=True, help_text="Date and time the book was checked out")
    return_date = models.DateTimeField(null=True, blank=True, help_text="Date and time the book was returned")

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

