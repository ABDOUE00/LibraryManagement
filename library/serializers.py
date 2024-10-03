from rest_framework import serializers
from .models import Book, Transaction
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model to convert model instances
    into JSON format and vice versa.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'copies_available']
        # It is generally better to specify fields explicitly to avoid exposing unnecessary data.

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to convert user instances
    into JSON format and vice versa.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'is_active']
        # Include only relevant fields that are necessary for the API responses.

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model to convert transaction instances
    into JSON format and vice versa.
    """
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']
        # Ensure that all relevant fields are included for transactions.

