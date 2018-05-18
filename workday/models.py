from django.db import models
from employee.models import Driver,Operator
from vehicle.models import Vehicle
from django.utils import timezone

# Create your models here.
class Workday(models.Model):
    zone=models.CharField(max_length=50)
    datestart=models.DateField(default=timezone.now)
    datefinish=models.DateField(null=True, blank=True)
    operator=models.ManyToManyField(Operator, null=True, blank=True)
    driver=models.ForeignKey(Driver, null=True, blank=True,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.zone)