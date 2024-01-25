from django.shortcuts import render

# Create your views here.

def home(request):

    # print(request.user.account)
    return render(request, 'home.html')