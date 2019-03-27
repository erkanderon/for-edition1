from django.shortcuts import render
from django.views import generic
from univer.forms import UserLoginForm, UserSignUpForm




class SearchPageView(generic.ListView):
	template_name = "search/search.html"
	signin_form = UserLoginForm
	signup_form = UserSignUpForm

	def get(self, request):
		signin_form = self.signin_form(None)
		signup_form = self.signup_form(None)
		return render(request, self.template_name, {'signin_form': signin_form, 'signup_form': signup_form})
