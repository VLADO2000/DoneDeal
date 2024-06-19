from django.views.generic import DeleteView, UpdateView, DetailView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class AccountView(DetailView):
    model = get_user_model()
    context_object_name = 'account'
    template_name = 'account/account_page.html'


class AccountUpdateView(UpdateView):
    model = get_user_model()
    fields = ['brand_name', 'email', 'role', 'description',]
    template_name = 'account/account_update.html'


class AccountDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'account/account_delete.html'
    success_url = reverse_lazy('home')
