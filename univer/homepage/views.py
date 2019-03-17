from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from univer.forms import UserLoginForm, UserSignUpForm
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout




class HomePageView(generic.ListView):
	#model = PostList
	#context_object_name = 'all_posts'
	template_name = "homepage/homepage.html"
	form_class = UserLoginForm
	signup_form = UserSignUpForm

	def get(self, request):
		form = self.form_class(None)
		signup_form = self.signup_form(None)
		return render(request, self.template_name, {'form': form, 'signup_form': signup_form})
