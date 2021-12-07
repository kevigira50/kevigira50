
# Create your models here.
from django.db import models


class Idafarmuser(models.Model):
    sessionId = models.CharField(max_length=255,null=True)
    servicecode = models.CharField(max_length=255, null=True)
    phooneNumber = models.CharField(max_length=225)
    level = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    sizeofland = models.CharField(max_length=225)
    names = models.CharField(max_length=225)
    idnumber = models.CharField(max_length=225)
    created_on = models.CharField(max_length=225)

    def __str__(self):
        return self.phonenumber


class Product(models.Model):
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


