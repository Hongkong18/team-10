from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Employee(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	availableTime = models.IntegerField()

class Volunteer(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	availableTime = models.IntegerField(default=0)
	
class Vendor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	
class Sponsor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()

class Event(models.Model):
	name = models.CharField(max_length=50)
	introduction = models.CharField(max_length=500)

	date = models.DateField(auto_now_add=True)
	employee = models.ManyToManyField(Employee)
	volunteer = models.ManyToManyField(Volunteer)
	vendor = models.ManyToManyField(Vendor)
	sponsor = models.ManyToManyField(Sponsor)


class Project(models.Model):
	name = models.CharField(max_length=50)
	introduction = models.CharField(max_length=500)

	startdate = models.DateField(auto_now_add=True)
	enddate = models.DateField(auto_now_add=True)
	employee = models.ManyToManyField(Employee)
	volunteer = models.ManyToManyField(Volunteer)
	vendor = models.ManyToManyField(Vendor)
	sponsor = models.ManyToManyField(Sponsor)