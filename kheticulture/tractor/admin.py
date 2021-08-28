from django.contrib import admin
from .models import Tractor
from .models import Attachments
from .models import Tractor_Attachments
from .models import Tractor_Types
from .models import Tractor_Sub_Types_Activities

admin.site.register(Tractor)
admin.site.register(Attachments)
admin.site.register(Tractor_Attachments)
admin.site.register(Tractor_Types)
admin.site.register(Tractor_Sub_Types_Activities)
