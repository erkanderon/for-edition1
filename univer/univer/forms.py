from django.contrib.auth.models import User
from django import forms

class UserLoginForm(forms.Form):

	login_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}))
	login_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre', 'class': 'form-control', 'minlength': '6'}))
	fields = ['username', 'password']


class UserSignUpForm(forms.ModelForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre', 'class': 'form-control', 'minlength': '6'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'E-posta Adresi', 'class': 'form-control'}))

	class Meta():
		model = User
		fields = ('username','password','email')