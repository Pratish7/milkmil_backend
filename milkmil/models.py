from django.db import models


class Guests(models.Model):

    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now_add=True)
    # image_url = models.CharField(max_length=2000, null=True, blank=True)


