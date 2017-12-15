from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import User

# Since we created our own user class, we should also create our own registration form for the user
# This way we can have the user enter any required information we desire
class RegisterForm(UserCreationForm):

    # We require from the user: first_name, last_name, phone_number, email, and password
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=10, required=True)

    # The UserCreationForm should already handle email and password for us

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')
