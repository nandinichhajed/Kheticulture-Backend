from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'job'

urlpatterns = [
    path('createjob/', views.create_job, name='createjob'),
    path('updatejob/', views.update_job, name='updatejob'),
    path('postinvoice/', views.post_invoice, name='postinvoice'),
]
