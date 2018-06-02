from rest_framework import serializers
from employee.models import Driver, Operator
from vehicle.models import Vehicle
from workday.models import Workday

#Prueba de ramas en Git
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('name', 'lastname','sex','age','birthday','dateadmission','phone','email','address','license')


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('name', 'lastname','sex','age','birthday','dateadmission','phone','email','address')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('serialnumber', 'weight','country','terminationdate')

class WorkdaySerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    driverid = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Driver.objects.all(), source='driver')
    vehicle = VehicleSerializer(read_only=True)
    vehicleid = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vehicle.objects.all(), source='vehicle')
    operator = OperatorSerializer(many=True,read_only=True)
    operatorid = serializers.PrimaryKeyRelatedField(many=True,write_only=True, queryset=Operator.objects.all(), source='operator')
    class Meta:
        model = Workday
        fields = ('id', 'zone', 'datestart', 'datefinish', 'operator','operatorid', 'driver','driverid','vehicle','vehicleid')