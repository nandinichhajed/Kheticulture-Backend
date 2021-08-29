from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tractor'

urlpatterns = [
    path('', views.all_tractors, name='all_tractors'),
    path('add/', views.add, name='add'),
    path('radiustractor/', views.get_all_tractor_within_radius),
    path('availabletractor/', views.get_available_tractors_within_radius),
    #url(r'^api/tractortypes$', tractor_types_list),
    #url(r'^api/tractorsubtypes$', tractor_subtypes_activities_list),
    #url(r'^api/tractor$', tractor_list),
    #url(r'^api/tractorwithinradius$', get_tractor_within_radious)
]
