from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm



class CustomAccountForm(SignupForm):
    
    brand_name = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=[(0, 'individual'),(1, 'company'),])
    