
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserAccount.urls')),
    path('', include('Core.urls')),
    path('', include('Transaction')),
]
