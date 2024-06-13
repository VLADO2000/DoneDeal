from allauth.account.adapter import DefaultAccountAdapter



class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data.get('email')
        user.set_password(data.get('password1'))
        user.brand_name = data.get('brand_name')
        user.role = data.get('role')

        if commit:
            user.save()
        
        return user
                          

