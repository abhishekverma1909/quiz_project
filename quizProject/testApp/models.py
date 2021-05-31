from django.db import models

# Create your models here.
class Javamcq(models.Model):
    question=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)

class Pythonmcq(models.Model):
    question=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)

class Cplusmcq(models.Model):
    question=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)

class Aptitudemcq(models.Model):
    question=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)
