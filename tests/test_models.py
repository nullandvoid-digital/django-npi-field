from django.db import models
from npi_field.modelfields import NPIField


class TestNPIModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    npi = NPIField(null=True, blank=True)
    name = models.CharField(max_length=100)


class TestPKModel(models.Model):
    npi = NPIField(unique=True)
    name = models.CharField(max_length=10)
