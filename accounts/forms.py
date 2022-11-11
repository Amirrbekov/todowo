from django import forms
from .models import Register, Login

class RegisterForm(forms.ModelForm):

    class Meta:

        model = Register
        fields = ('fullname', 'mail', 'username', 'password', 'confirm')

class LoginForm(forms.ModelForm):

    class Meta:

        model = Login
        fields = ('username', 'password')