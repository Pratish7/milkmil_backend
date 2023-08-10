from django.db import models


class Guests(models.Model):

    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now_add=True)
    # image_url = models.CharField(max_length=2000, null=True, blank=True)


class Milk(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    quantity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Vehicle(models.Model):

    type = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    num_passengers = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(null=True, blank=True)
    out_kms = models.FloatField(null=True, blank=True)

    