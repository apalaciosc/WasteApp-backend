from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

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

urlpatterns = [
	path('v1/workdays', workday_list,name='workday_list'),
    path('v1/workdays/<int:pk>', workday_detail,name='workday_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
