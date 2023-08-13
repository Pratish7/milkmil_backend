from django.db import models
from django.contrib.postgres.fields import ArrayField


class Guests(models.Model):

    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255, null=True, blank=True)
    organization = models.CharField(max_length=255)
    in_date = models.DateField(auto_now_add=True)
    in_time = models.TimeField(auto_now_add=True)
    out_date = models.DateField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    # image_url = models.CharField(max_length=2000, null=True, blank=True)


class Milk(models.Model):

    id = models.AutoField(primary_key=True)
    quantity = models.FloatField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)


class Vehicle(models.Model):

    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    num_passengers = models.IntegerField()
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(null=True, blank=True)
    out_kms = models.FloatField(null=True, blank=True)


class Keys(models.Model):

    key_types = (
        ('SPINNING' , 'SPINNING'),
        ('CARDING', 'CARDING'),
        ('AUTOCONER', 'AUTOCONER'),
        ('NEW GODOWN', 'NEW GODOWN'),
        ('CANTEEN', 'CANTEEN'),
        ('COMBER', 'COMBER'),
        ('FM ROOM', 'FM ROOM'),
        ('OFFICE', 'OFFICE'),
        ('SIMPLEX', 'SIMPLEX'),
        ('STORE ROOM', 'STORE ROOM'),
    )

    date = models.DateField(auto_now_add=True)
    key_type = models.CharField(choices=key_types)
    taken_time = models.DateTimeField(auto_now_add=True)
    returned_time = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class ReturnableMaterials(models.Model):

    status_choices = (
        ('YET TO BE RETURNED', 'YET TO BE RETURNED'),
        ('RETURNED / COMPLETED', 'RETURNED / COMPLETED'),
    )

    id = models.AutoField(primary_key=True)
    out_date = models.DateField(auto_now_add=True)
    out_time = models.TimeField(auto_now_add=True)
    gate_pass_num = models.IntegerField()
    in_date = models.DateField(blank=True, null=True)
    in_time = models.TimeField(blank=True, null=True)
    status = models.CharField(choices=status_choices)


class MaterialOutward(models.Model):

    status_choices = (
        ('QUEUE', 'QUEUE'),
        ('DISPATCHED / COMPLETED', 'DISPATCHED / COMPLETED'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    invoice_num = models.CharField()
    status = models.CharField(choices=status_choices)


class MaterialInward(models.Model):

    date = models.DateField(auto_now_add=True)
    # vehicle_picture
    invoice_num = models.CharField()
    in_time = models.TimeField(auto_now_add=True)
    out_time = models.TimeField(blank=True, null=True)


class MasterData(models.Model):

    key = models.CharField(max_length=255, primary_key=True)
    values = ArrayField(models.CharField())
