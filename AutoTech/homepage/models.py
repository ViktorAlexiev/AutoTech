from django.db import models

class b_data(models.Model):
    RK = models.IntegerField()
    RN = models.CharField(max_length=255)
    Marka = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    G_PR = models.IntegerField()
    KM = models.IntegerField()
    Kupe = models.CharField(max_length=255)
    Rama = models.CharField(max_length=255)
    Dvigatel = models.CharField(max_length=255)
    Descr = models.TextField()
    Problema = models.TextField()
    R_DATA = models.DateTimeField()
    
class c_data(models.Model):
    RK = models.IntegerField()
    ime = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    
class w_data(models.Model):
    RK = models.IntegerField()
    W_ID = models.IntegerField()
    WORK = models.TextField()
    PRICE = models.IntegerField()
    
class p_data():
    RK = models.IntegerField()
    W_ID = models.IntegerField()
    PART = models.CharField(max_length=255)
    PRICE = models.IntegerField()