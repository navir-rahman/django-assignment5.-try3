from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, Review, BorrowedBook
from .forms import CommentForm, BuyForm
from Transaction.forms import DepositForm
from UserAccount.models import UserAccount
from django.utils import timezone 

from django.conf import settings
from django.core.mail import send_mail


def detail_book_view(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)
    comment_form = CommentForm()
    buy_form = BuyForm()

    is_returned = False
    if request.user.is_authenticated:
        user_instance = UserAccount.objects.get(user=request.user)
        borrowed_books = BorrowedBook.objects.filter(user_account=user_instance, book=book)

        is_returned = borrowed_books.exists()  

    # print(is_returned)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'buy_form' in request.POST:
                buy_form = BuyForm(data=request.POST)
                if buy_form.is_valid():
                    buy = buy_form.save(commit=False)
                    userInstance = UserAccount.objects.get(user=request.user)
                    if isinstance(userInstance, tuple):
                            userInstance, created = userInstance

                    buy.user = userInstance
                    amount = buy_form.cleaned_data['amount']
                    quantity = buy_form.cleaned_data['quantity']
                    total_amount= amount * quantity
                    # print(amount)
                    buy.user.balance -= total_amount
                    buy.user.save()

                    # borrow the book functionality
                    now = timezone.now()
                    BorrowedBook.objects.create(
                        user_account=userInstance,
                        book=book,  
                        borrowing_date=now,
                        isReturned=False
                    )

                    messages.success(request, "Book purchased successfully")
    # email notification
                    subject = 'Book Borrow'
                    message = f'Hi {request.user.username} you have successfully borrowed {book} at {now}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.user.email, ]
                    send_mail( subject, message, email_from, recipient_list )


                    return HttpResponseRedirect(request.path)

                else:
                        messages.error(request, "Invalid buy form data")

            elif 'comment_form' in request.POST:    
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)

                    if request.user.is_authenticated:
                        user_account = UserAccount.objects.get(user=request.user)
                        if isinstance(user_account, tuple):
                            user_account, created = user_account

                        new_comment.user = user_account
                        new_comment.user.email = request.user.email
                        new_comment.book = book
                        new_comment.save()
                        messages.success(request, "Comment created successfully")
                        # email notification
                        subject = 'comment created successfully'
                        message = f'Hi {request.user.username} you have successfully made a new comment'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [request.user.email, ]
                        send_mail( subject, message, email_from, recipient_list )

                    else:
                        messages.error(request, "Sorry you are not logged in")
                    return HttpResponseRedirect(request.path)
            else:
                 messages.info(request, "Sorry you are not logged in")

    context = {'book': book, 'reviews': reviews, 'form': comment_form, 'buy_form': buy_form, 'isReturned':is_returned}
    return render(request, 'book_details.html', context)


def borrowHistory(request):
     userInstance = UserAccount.objects.get(user=request.user)
     borrowed = BorrowedBook.objects.filter(user_account = userInstance)
    #  print(borrowed)
     return render(request, 'borrowHistory.html', { 'borrowedBook': borrowed})

def return_book(request, id = None):
    userInstance = UserAccount.objects.get(user=request.user)
    borrowed = BorrowedBook.objects.filter(user_account = userInstance)

    theBook = get_object_or_404(BorrowedBook, pk=id)
    book_price = get_object_or_404(Book, borrowedbook=theBook).borrowing_price

    userInstance.balance += book_price 
    userInstance.save()

    now = timezone.now()
    theBook.isReturned = True
    theBook.returning_date = now
    theBook.save()
    
    return render(request, 'borrowHistory.html', { 'borrowedBook': borrowed})
