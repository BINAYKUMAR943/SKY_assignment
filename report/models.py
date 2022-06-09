from django.db import models


class Report(models.Model):
    id=models.UUIDField(primary_key=True)
    team=models.CharField(max_length=255)
    machine=models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    ip=models.GenericIPAddressField()
    state=models.CharField(max_length=255)
    cloud_name=models.CharField(max_length=255)