from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import AccountView

urlpatterns = [
    path('account/<uuid:pk>/', login_required(AccountView.as_view()), name='account_detail'),
]