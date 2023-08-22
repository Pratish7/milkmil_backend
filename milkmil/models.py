from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
import pytz


class TimeFieldWithoutMicroseconds(models.TimeField):
    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, datetime.time):
            return value.replace(microsecond=0)
        return super().get_db_prep_value(value, connection, prepared)
    

class Guests(models.Model):

    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    in_date = models.DateField(auto_now_add=True)
    in_time = models.TimeField(auto_now_add=True)
    out_date = models.DateField(null=True, default=None)
    out_time = models.TimeField(null=True, default=None)
    image = models.TextField(null=True, blank=True)

@receiver(post_save, sender=Guests)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.in_time = instance.in_time.replace(microsecond=0)
        instance.save()


class Milk(models.Model):

    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

@receiver(post_save, sender=Milk)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.time = instance.time.replace(microsecond=0)
        instance.save()


class Vehicle(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    num_passengers = models.IntegerField()
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(null=True, blank=True)
    out_kms = models.FloatField(null=True, blank=True)

@receiver(post_save, sender=Vehicle)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.in_time = instance.in_time.replace(microsecond=0)
        instance.out_time = instance.out_time.replace(microsecond=0)
        instance.save()


class Keys(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    person_name = models.CharField(max_length=255)
    key_type = models.CharField()
    taken_time = models.TimeField(auto_now_add=True)
    returned_time = models.TimeField(null=True, blank=True)

@receiver(post_save, sender=Keys)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.taken_time = instance.taken_time.replace(microsecond=0)
        instance.returned_time = instance.returned_time.replace(microsecond=0)
        instance.save()    


class KeysMaster(models.Model):

    id = models.AutoField(primary_key=True)
    key_type = models.CharField()
    quantity = models.IntegerField()
    bar_code = models.TextField(null=True, blank=True)


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
    status = models.CharField(choices=status_choices, default='YET TO BE RETURNED')

@receiver(post_save, sender=ReturnableMaterials)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.out_time = instance.out_time.replace(microsecond=0)
        instance.in_time = instance.in_time.replace(microsecond=0)
        instance.save()


class MaterialOutward(models.Model):

    status_choices = (
        ('QUEUE', 'QUEUE'),
        ('DISPATCHED / COMPLETED', 'DISPATCHED / COMPLETED'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    invoice_num = models.CharField()
    status = models.CharField(choices=status_choices, default='QUEUE')

@receiver(post_save, sender=MaterialOutward)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.time = instance.time.replace(microsecond=0)
        instance.save()


class MaterialInward(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    image = models.TextField(null=True, blank=True)
    invoice_num = models.CharField(max_length=255)
    in_time = models.TimeField(auto_now_add=True)
    out_time = models.TimeField(blank=True, null=True)

@receiver(post_save, sender=MaterialInward)
def remove_microseconds_save(sender, instance, created, **kwargs):
    if created:
        instance.in_time = instance.in_time.replace(microsecond=0)
        instance.out_time = instance.out_time.replace(microsecond=0)
        instance.save()


class MasterData(models.Model):

    key = models.CharField(max_length=255, primary_key=True)
    values = ArrayField(models.CharField())


class BarCode(models.Model):

    id = models.AutoField(primary_key=True)
    barcode = models.TextField()
    invoice_num = models.CharField()


class Employees(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
