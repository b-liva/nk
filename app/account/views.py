from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import reverse
from account.forms.form import CustomAuthenticationForm


class CbvLogin(LoginView):
    template_name = 'accounts/cbv_login.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        return reverse('home')


class CbvLogout(LogoutView):

    def get_next_page(self):
        return reverse('cbv-login')
