import uuid
from django.db import models

# Create your models here.

class Add_Doctors_Details(models.Model):

    doctorID = models.CharField(max_length=100)
    doctorname = models.CharField(max_length=100)
    doctoraddress = models.CharField(max_length=500)
    mobileno = models.CharField(max_length=20)
    emailid = models.CharField(max_length=100)
    doctorage = models.IntegerField()
    doctorgender = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200)


class Doc_MRI_ScanValue(models.Model):

    analysisvalue = models.CharField(max_length=5000)
    uniquecontors = models.CharField(max_length=5000)




