from django.forms import ModelForm

from django.contrib.auth import get_user_model

class AccountForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'label', 'role', 'description',]