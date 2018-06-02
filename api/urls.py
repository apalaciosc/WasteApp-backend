from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

#WorkDay
workday_list = views.WorkdayViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

workday_detail = views.WorkdayViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

#Driver
driver_list = views.DriverViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

driver_detail = views.DriverViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

#Operator
operator_list = views.OperatorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

operator_detail = views.OperatorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

#Vehicle
vehicle_list = views.VehicleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

vehicle_detail = views.VehicleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
	path('v1/workdays', workday_list,name='workday_list'),
    path('v1/workdays/<int:pk>', workday_detail,name='workday_detail'),
    path('v1/drivers', driver_list,name='driver_list'),
    path('v1/drivers/<int:pk>', driver_detail,name='driver_detail'),
    path('v1/operators', operator_list,name='operator_list'),
    path('v1/operators/<int:pk>', operator_detail,name='operator_detail'),
    path('v1/vehicles', vehicle_list,name='vehicle_list'),
    path('v1/vehicles/<int:pk>', vehicle_detail,name='vehicle_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
