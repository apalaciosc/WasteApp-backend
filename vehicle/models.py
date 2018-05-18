from django.db import models

# Create your models here.
class Vehicle(models.Model):
    serialnumber=models.CharField(max_length=50)
    weight=models.IntegerField()
    country=models.CharField(max_length=10)
    terminationdate=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.serialnumber)