from django.urls import path
from . import views

app_name = 'tractor'

urlpatterns = [
    path('', views.all_tractors, name='all_tractors'),
	path('add/', views.add, name='add'),
    path('all_tractor_within_radious/', views.get_all_tractor_within_radius, name='get_all_tractor_within_radius'),
    path('tractor_available_within_radious/', views.get_available_tractors_within_radius, name='get_available_tractors_within_radius'),
    path('details/', views.get_tractor_details, name='get_tractor_details'),
    path('update_tractor_availabilty/', views.update_tractor_availabilty, name='update_tractor_availabilty'),
]
