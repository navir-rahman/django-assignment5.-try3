from django.db import models
from django.contrib.auth.models import User
from Books.models import Book

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True) 
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) 
    borrowed_books = models.ManyToManyField(Book, related_name='borrowers', through='BorrowedBook')
    
    def __str__(self):
        return str(self.account_no)
    
