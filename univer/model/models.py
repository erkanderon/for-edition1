from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class University(models.Model):
	pop_status = (
		(1, 'Half Star'),
		(2, 'One Star'),
		(3, 'One and Half Star'),
		(4, 'Two Star'),
		(5, 'Two and Half Star'),
		(6, 'Three Star'),
		(7, 'Three and Half Star'),
		(8, 'Four Star'),
		(9, 'Four and Half Star'),
		(10, 'Five Star')
	)

	university_name = models.CharField(max_length=50)
	university_description = models.TextField(null=True, blank=True)
	university_logo = models.CharField(max_length=150)
	university_popularity = models.IntegerField(choices=pop_status)

	def __str__(self):
		return self.university_name

class Teacher(models.Model):
	# Course teachers
	pop_status = (
		(1, 'Half Star'),
		(2, 'One Star'),
		(3, 'One and Half Star'),
		(4, 'Two Star'),
		(5, 'Two and Half Star'),
		(6, 'Three Star'),
		(7, 'Three and Half Star'),
		(8, 'Four Star'),
		(9, 'Four and Half Star'),
		(10, 'Five Star')
	)

	teacher_title = models.CharField(max_length=20, null=True)
	teacher_name = models.CharField(max_length=30)
	teacher_surname = models.CharField(max_length=30)
	teacher_description = models.TextField(blank=True, null=True)
	teacher_image = models.CharField(max_length=150)
	teacher_popularity = models.IntegerField(choices = pop_status)
	teacher_university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.teacher_title + ' ' +self.teacher_name + ' ' +self.teacher_surname

# === Models for Learning app ===

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
	course_teacher = models.ManyToManyField(Teacher, blank=True)
	course_logo = models.CharField(max_length=150, null=True)


	'''def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk':self.pk})'''

	def __str__(self):
		return self.course_title




