from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomAccountForm(SignupForm):
    
    brand_name = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=[(0, 'individual'),(1, 'company'),])
    
    def save(self, request):
        user = super(CustomAccountForm, self).save(request)
        user.brand_name = self.cleaned_data['brand_name']
        user.role = self.cleaned_data['role']
        user.save()
        return user
    
class CustomAccountChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields + 'brand_name' + 'description' + 'role'