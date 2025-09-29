from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500'
            })


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500'
            })
