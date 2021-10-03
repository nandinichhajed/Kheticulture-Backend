from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tractor'

urlpatterns = [
    path('', views.all_tractors, name='all_tractors'),
    path('add/', views.add, name='add'),
    path('radiustractor/', views.get_all_tractor_within_radius, name='radiustractor'),
    path('availabletractor/', views.get_available_tractors_within_radius, name='availabletractor'),
    path('updaterating/', views.update_tractor_rating, name='updaterating'),
]
