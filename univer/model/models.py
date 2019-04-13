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

	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	logo = models.CharField(max_length=150)
	popularity = models.IntegerField(choices=pop_status, default=10)

	def __str__(self):
		return self.name

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

	title = models.CharField(max_length=20, null=True)
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	description = models.TextField(blank=True, null=True)
	image = models.CharField(max_length=150)
	popularity = models.IntegerField(choices = pop_status, default=10)
	university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title + ' ' +self.name + ' ' +self.surname

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
	course_level = (
		('Beginner', 'Beginner'),
		('Mixed', 'Mixed'),
		('Hard', 'Hard')
	)
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
	tags = (
		('Course', 'Course'),
		('Specialization', 'Specialization'),
		('Certificated Course', 'Certificated Course')
	)

	owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField(default=29.99)
	price_currency = models.CharField(max_length=5, choices=price_currencies, default='TL')
	pub_date = models.DateField(auto_now_add=True)
	status = models.IntegerField(choices=course_status)
	teacher = models.ManyToManyField(Teacher, blank=True)
	belongs_to = models.ForeignKey(University, null=True, on_delete=models.SET_NULL)
	count_subscriber = models.IntegerField(default=0, blank=True)
	level = models.CharField(choices=course_level, default='Beginner', max_length=20)
	popularity = models.IntegerField(choices=pop_status, default=10)
	tag = models.CharField(choices=tags, default='Course', max_length=20)
	logo = models.CharField(max_length=150, null=True)


	'''def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk':self.pk})'''

	def __str__(self):
		return self.title

