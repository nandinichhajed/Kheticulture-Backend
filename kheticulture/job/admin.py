from django.contrib import admin
from .models import Job, JobImage, JobVideo

admin.site.register(Job)
admin.site.register(JobImage)
admin.site.register(JobVideo)