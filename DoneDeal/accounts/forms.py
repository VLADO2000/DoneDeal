from allauth.account.forms import SignupForm
from django import forms


class CustomAccountForm(SignupForm):
    
    brand_name = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=[(0, 'individual'),(1, 'company'),])
    
    def safe(self,request):
        user = super(CustomAccountForm, self).save(request)
        user.brand_name = self.cleaned_data['brand_name']
        user.role = self.cleaned_data['role']
        user.save()
        return user