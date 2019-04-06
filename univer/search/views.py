from django.shortcuts import render
from django.views import generic
from univer.forms import UserLoginForm, UserSignUpForm

from search.documents import CourseDocument


class SearchPageView(generic.ListView):
	template_name = "search/search.html"
	signin_form = UserLoginForm
	signup_form = UserSignUpForm

	def get(self, request):
		signin_form = self.signin_form(None)
		signup_form = self.signup_form(None)
		return render(request, self.template_name, {'signin_form': signin_form, 'signup_form': signup_form})



def search(request):

	q = request.GET.get('q')

	if q:
		courses = CourseDocument.search().query('match', course_description=q)
	else:
		courses = ''

	return render(request, 'search/search.html', {'courses': courses})
