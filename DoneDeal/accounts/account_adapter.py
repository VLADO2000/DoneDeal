from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = get_user_model().objects.create_user(
            email = data.get('email'),
            password = data.get('password1'),
            brand_name = data.get('brand_name'),
            role = data.get('role'),
            )
       
        return user

