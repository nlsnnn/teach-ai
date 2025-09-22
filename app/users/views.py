from django.contrib.auth.views import LoginView, LogoutView  # noqa: F401
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from .forms import CustomUserCreationForm


class UserRegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = ""
    # success_url = ""


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    # success_url = ""

