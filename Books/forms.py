from django import forms
from .models import Review
from Transaction.models import Transaction

        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['rating', 'comment']

class BuyForm(forms.ModelForm):
    quantity = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ['quantity', 'amount']
