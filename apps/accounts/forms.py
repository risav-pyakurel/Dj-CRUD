from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    pass
    # email = forms.EmailField(
    #     widget = forms.EmailInput
    # )
    # password = forms.CharField(
    #     widget= forms.PasswordInput
    # )
