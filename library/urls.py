from django.urls import path
from .views import (
    BookListCreateView, 
    BookRetrieveUpdateDestroyView,
    UserListCreateView, 
    UserRetrieveUpdateDestroyView,
    CheckoutBookView, 
    ReturnBookView, 
    AvailableBooksView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Book management URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # List and create books
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),  # Retrieve, update, and delete a book

    # User management URLs
    path('users/', UserListCreateView.as_view(), name='user-list-create'),  # List and create users
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),  # Retrieve, update, and delete a user

    # Checkout and return URLs
    path('checkout/', CheckoutBookView.as_view(), name='checkout-book'),  # Checkout a book
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),  # Return a checked-out book

    # Available books URL
    path('available-books/', AvailableBooksView.as_view(), name='available-books'),  # View available books

    # JWT Authentication URLs
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login and obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]

