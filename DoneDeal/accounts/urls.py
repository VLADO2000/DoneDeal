from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import AccountView, AccountUpdateView, AccountDeleteView

urlpatterns = [
    path('account/<uuid:pk>/', login_required(AccountView.as_view()), name='account_detail'),
    path('account/profile-update/<uuid:pk>/', AccountUpdateView.as_view(), name='account_update'),
    path('account/profile-delete/<uuid:pk>/', AccountDeleteView.as_view(), name='account_delete'),
]