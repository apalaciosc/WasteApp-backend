from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=70)
    sex=models.CharField(max_length=10)
    age=models.IntegerField()
    birthday=models.DateTimeField()
    dateadmission=models.DateTimeField()
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=30)
    address=models.TextField()

    class Meta:
        abstract = True

class Driver(Person):
    license=models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)

class Operator(Person):
    pass

    def __str__(self):
        return '{}'.format(self.name)
		