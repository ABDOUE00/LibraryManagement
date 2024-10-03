from django.test import TestCase
from .models import Book
from datetime import date

class BookTests(TestCase):
    def test_add_book(self):
        book = Book.objects.create(
            title='Test Book', 
            author='Test Author', 
            published_date=date.today(),
            copies_available=5
        )
        self.assertEqual(Book.objects.count(), 1)

    def test_edit_book(self):
        book = Book.objects.create(
            title='Test Book', 
            author='Test Author', 
            published_date=date.today(),
            copies_available=5
        )
        book.title = 'Updated Title'
        book.save()
        self.assertEqual(Book.objects.get(id=book.id).title, 'Updated Title')

    def test_delete_book(self):
        book = Book.objects.create(
            title='Test Book', 
            author='Test Author', 
            published_date=date.today(),
            copies_available=5
        )
        book_id = book.id
        book.delete()
        self.assertFalse(Book.objects.filter(id=book_id).exists())
