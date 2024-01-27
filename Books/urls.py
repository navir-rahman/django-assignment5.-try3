from django.urls import path
from .views import detail_book_view, borrowHistory, return_book
urlpatterns = [
    path('view/<int:id>', detail_book_view, name='view_book'),
    path('borrowHistory/', borrowHistory, name='borrowHistory'),
    path('returnBook/<int:id>', return_book, name='returnBook'),
]
