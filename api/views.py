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
     
    #detail_route decorator stands for single instances, using pk element in its URL pattern
    #@detail_route(methods=['post'])
    #def set_comment(self, request, pk=None):

        #get workday object
    #    my_workday = self.get_object()  

    #    serializer = OperatorSerializer(data=request.data)                 
    #    if serializer.is_valid():
    #        serializer.save(post=my_workday)
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            


