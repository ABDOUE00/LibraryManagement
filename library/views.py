from rest_framework import generics, serializers, filters
from .models import Book, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class BookListCreateView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book.
    Permissions: Only authenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a book.
    Permissions: Only authenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    """
    View to list all users or create a new user.
    Permissions: Only authenticated users can access this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a user.
    Permissions: Only authenticated users can access this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CheckoutBookView(generics.CreateAPIView):
    """
    View to checkout a book for the authenticated user.
    If the book is available, it will decrease the available copies.
    """
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.copies_available > 0:
            book.copies_available -= 1
            book.save()
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("No copies available")

class ReturnBookView(generics.UpdateAPIView):
    """
    View to return a checked-out book.
    It will update the return date and increase the available copies.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.return_date = timezone.now()
        instance.save()

        book = instance.book
        book.copies_available += 1
        book.save()

class AvailableBooksView(generics.ListAPIView):
    """
    View to list all available books (copies > 0).
    Permissions: Only authenticated users can access this view.
    It supports search functionality.
    """
    queryset = Book.objects.filter(copies_available__gt=0)  
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'isbn']  
