
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('UserAccount/', include('UserAccount.urls')),
    path('books/', include('Books.urls')),
    path('', include('Core.urls')),
    path('Transaction/', include('Transaction.urls')),
]
