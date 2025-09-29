from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
