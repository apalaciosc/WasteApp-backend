from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from employee.models import Driver, Operator
from vehicle.models import Vehicle
from workday.models import Workday
from .serializers import DriverSerializer, OperatorSerializer, VehicleSerializer,WorkdaySerializer


class WorkdayViewSet(viewsets.ModelViewSet):
    #This view automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
     
    queryset = Workday.objects.all()
    serializer_class = WorkdaySerializer          

class DriverViewSet(viewsets.ModelViewSet):
    #This view automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
     
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class OperatorViewSet(viewsets.ModelViewSet):
    #This view automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
     
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    #This view automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
     
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

