from tkinter import CASCADE
from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    userid = models.CharField(max_length=50)
    firstname = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20)
    dob = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Feeback_Model(models.Model):
    name = models.CharField(max_length=50)
    diseasetype = models.CharField(max_length=50)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    stars1 = models.CharField(max_length=20)

class MRI_ScanValue(models.Model):
    Brain_Userd = models.ForeignKey(UserRegistration, CASCADE)
    analysisvalue = models.CharField(max_length=5000)
    uniquecontors = models.CharField(max_length=5000)

class Post_MRIimageScan(models.Model):
    Patient_Name= models.CharField(max_length=500)
    Patient_Age = models.IntegerField()
    AnyauseofSymptoms =models.CharField(max_length=1000)
    UploadBrainMRIImage = models.ImageField()
    Recommendation = models.CharField(max_length=5000)





