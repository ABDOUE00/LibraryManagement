from django.contrib import admin
from .models import Book, Transaction  

# Registering the Book and Transaction models to the admin site
admin.site.register(Book)
admin.site.register(Transaction)
