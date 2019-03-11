from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from univer.forms import UserLoginForm
from django.views.generic import View
from django.contrib.auth import login, authenticate




class HomePageView(generic.ListView):
	#model = PostList
	#context_object_name = 'all_posts'
	template_name = "homepage/homepage.html"
	form_class = UserLoginForm

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

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

		return render(request, self.template_name, {'form': UserLoginForm})
