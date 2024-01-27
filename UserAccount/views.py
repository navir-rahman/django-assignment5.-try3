from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.conf import settings
from django.core.mail import send_mail

class UserRegistrationView(FormView):
    template_name = 'signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('signUp')

    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()

        login(self.request, user)

        subject = 'Deposit'
        message = f'Hi {self.request.user.username}, you have successfully created a new account'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return super().form_valid(form) 
    

class UserLoginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('home')

def custom_logout(request):
    logout(request)
    return redirect(reverse('home'))


class UserUpdateView(View):
    template_name = 'profile.html'
    
    def get(self, request):
        form =UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            reverse_lazy('profile') 

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ChangePasswordForm(PasswordChangeView):
    template_name = "password_reset.html"
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        response = super().form_valid(form)
        subject = 'password reset'
        message = f' you have successfully created a new account'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return response
    def form_invalid(self, form):
        return render(self.request, self.template_name)

