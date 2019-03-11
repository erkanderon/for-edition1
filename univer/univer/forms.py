from django.contrib.auth.models import User
from django import forms

class UserLoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre', 'class': 'form-control', 'minlength': '6'}))
	fields = ['username', 'password']