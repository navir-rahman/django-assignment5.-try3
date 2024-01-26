from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from .models import Transaction
from django.contrib import messages
from .forms import DepositForm
from UserAccount.models import UserAccount
from django.urls import reverse_lazy

class DepositView(View):
    template_name = 'transfer.html'
    # success_url = reverse_lazy('home')
    form_class = DepositForm
    model = Transaction
    def get(self, request):
        form = DepositForm()
        return render(request, self.template_name, {'form': form, 'title': 'Deposit'})
    def post(self, request):
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user = request.user.account
            # account = UserAccount.objects.filter(account=user)
            user.balance += amount
            user.save()
        return render(request, self.template_name, {'form': form, 'title': 'Deposit'})
class WithdrawView(View):
    template_name = 'transfer.html'
    # success_url = reverse_lazy('home')
    form_class = DepositForm
    model = Transaction
    def get(self, request):
        form = DepositForm()
        return render(request, self.template_name, {'form': form, 'title': 'Deposit'})
    def post(self, request):
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user = request.user.account
            # account = UserAccount.objects.filter(account=user)
            user.balance -= amount
            user.save()
        return render(request, self.template_name, {'form': form, 'title': 'Deposit'})


# class TransferMoneyView(View):
#     template_name = 'transactions/transfermoney.html'
#     def get(self, request):
#         form = TransferMoneyForm
#         return render(request, self.template_name, {'form': form, 'title': 'transfer'})
    
#     def post(self, request):
#         form = TransferMoneyForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data['amount']
#             to_user_id = form.cleaned_data['to_user_id']
#             current_user = request.user.account

#             try:
#                 to_account = UserBankAccount.objects.get(account_no=to_user_id)
                
#                 current_user.balance -= amount
#                 current_user.save()

#                 to_account.balance += amount
#                 to_account.save()

#                 Transaction.objects.create(
#                     account = current_user,
#                     amount =    amount,
#                     balance_afert_transaction = current_user.balance,
#                     transaction_type = "TRANSFER" 

#                 )


#                 Transaction.objects.create(
#                     account = to_account,
#                     amount =    amount,
#                     balance_afert_transaction = to_account.balance,
#                     transaction_type = "RECEIVED" 

#                 )
#                 messages.success(request, 'Successfully transferred amount')
                
#             except UserBankAccount.DoesNotExist:
#                 messages.error(request, 'user not found')
        

#             return render(request, self.template_name, {'form': form, 'title': 'Transfer Money'})