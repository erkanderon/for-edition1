from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# === Models for Blog app ===

class Course(models.Model):
	"""
	Course Model for each courses
	"""
	price_currencies = (
		('$', 'Dolar'),
		('€', 'Euro'),
		('TL', 'Türk Lirası')
	)
	course_status = (
		(1, 'Show'),
		(2, 'Hide')
	)

	course_owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	course_title = models.CharField(max_length=100)
	course_description = models.TextField(blank=True, null=True)
	course_price = models.FloatField(default=29.99)
	price_currency = models.CharField(max_length=5, choices=price_currencies)
	pub_date = models.DateField(auto_now_add=True)
	course_status = models.IntegerField(choices=course_status)


	'''def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk':self.pk})'''

	def __str__(self):
		return self.course_title