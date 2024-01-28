from django.db import models
from UserAccount.models import UserAccount
# from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category')
    description = models.TextField()
    image = models.ImageField(upload_to='books/media/', null=True, blank=True)
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.user.username} - {self.book.title}"

class BorrowedBook(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateField(auto_now_add=True)
    returning_date = models.DateField(default=None, blank=True, null=True)
    isReturned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_account} - {self.book} - {self.borrowing_date}"

