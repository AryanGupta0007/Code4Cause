from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    college = models.CharField(max_length=64)
    university = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    year = models.IntegerField(max_length=64)


class College(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
