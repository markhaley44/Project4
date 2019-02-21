from django.db import models


class BuildingAdmin(models.Model):
    tenantsName = models.CharField(max_length=100)
    unitNumber = models.IntegerField
    maintenanceStaff = models.CharField(max_length=100)

    def __str__(self):
        return self.tenantsName


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField
    unit = models.CharField(max_length=50)
    serviceIssue = models.TextField(max_length=600)

    def __str__(self):
        return self.serviceIssue


class MaintenanceStaff(models.Model):
    serviceIssue = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='maintenanceStaff')

    def __str__(self):
        return self.serviceIssue
