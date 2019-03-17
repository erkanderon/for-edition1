from django.shortcuts import render, redirect
from univer.forms import UserLoginForm, UserSignUpForm
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.views import generic
# Create your views here.




class LoginView(generic.ListView):

	template_name = "homepage/homepage.html"
	form_class = UserLoginForm

	def get_queryset(self):
		return None

	def post(self, request):
		form  = self.form_class(request.POST)

		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password = password)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')

		return render(request, self.template_name, {'form': form})

class SignUpView(generic.ListView):

	template_name = "homepage/homepage.html"
	form_class = UserSignUpForm

	def get_queryset(self):
		return None

	def post(self, request):
		form  = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit = False)

			# cleaned normalized data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']

			user.email = email
			user.set_password(password)
			user.save()

			# returns User object if the credentials are true

			user = authenticate(username=username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')

		return render(request, self.template_name, {'form': form})

class LogoutView(View):

	# display blank form
	def get(self, request):
		if self.request.user.is_authenticated:
			logout(self.request)
		return redirect('/')