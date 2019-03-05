from django.shortcuts import render
from django.views import generic
from .models import *





class HomePageView(generic.ListView):
	#model = PostList
	#context_object_name = 'all_posts'
	template_name = "homepage/homepage.html"

	def get_queryset(self):
		return None