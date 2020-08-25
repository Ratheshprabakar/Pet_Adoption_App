from django.db import models

class pet(models.Model):
	SEX_CHOICES = [('M','Male'),('F','Female')]
	name= models.CharField(max_length=100)
	submitter=models.CharField(max_length=100)
	species=models.CharField(max_length=30)
	submission_date=models.DateTimeField()
	description=models.TextField()
	breed=models.CharField(max_length=30, blank=True)
	sex=models.CharField(max_length=1,choices=SEX_CHOICES,blank=True)
	age=models.IntegerField(null=True)
	vaccination=models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
	name=models.CharField(max_length=30)
