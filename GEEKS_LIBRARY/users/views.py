from http.client import responses
from lib2to3.fixes.fix_input import context

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models, middlewares

class RegisterView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        qualifications = form.cleaned_data['qualifications']
        if qualifications == 'Junior':
            self.object.qualifications = 'Junior-300$'
        elif qualifications == 'Middle':
            self.object.qualifications = 'Middle-1000$'
        elif qualifications == 'Senior':
            self.object.qualifications = 'Senior-2000$'
        else:
            self.object.qualifications = 'у вас нет квалификации'
        self.object.save()
        return response

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse("users:user_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

