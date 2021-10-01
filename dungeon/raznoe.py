from django.contrib.auth.views import LogoutView
from django.views import generic
from .forms import CreateUser
from django.shortcuts import reverse

class CustomLogout(LogoutView):
    template_name = 'shlak/landing.html'

class Signup(generic.CreateView):
    template_name ='registration/signup.html'
    form_class = CreateUser

    def get_success_url(self):
        return reverse('login')