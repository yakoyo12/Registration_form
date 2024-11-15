from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
