from django.views.generic import DeleteView
from django.contrib.auth import get_user_model



class AccountView(DeleteView):
    model = get_user_model()
    context_object_name = 'account'
    template_name = 'account/account_page.html'