#from django.db import models

# Create your models here.


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    ssn = models.CharField(primary_key=True, max_length=10)
    uname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=10, blank=True, null=True)
    upassword = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'users'
    def __str__(self):
        return "ssn : "+self.ssn+"name : "+self.uname+"age : "+self.age