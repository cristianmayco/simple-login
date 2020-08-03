from django import forms
from .models import User


class RegisterUserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email', 'password')
