from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    height = models.CharField(max_length=255, null=True)
    average_earning = models.CharField(max_length=255, null=True)
    clothes_expenses = models.CharField(max_length=255, null=True)
    makeup_expenses = models.CharField(max_length=255, null=True)
    creams_expenses = models.CharField(max_length=255, null=True)

    note = models.CharField(max_length=255, null=True)




    class Meta:
        db_table = "firstone_person"


class Activity(models.Model):
    records = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    execution = models.CharField(max_length=100, null=True)
    createdat = models.DateTimeField(auto_now_add=True)
    finishedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "activity"
