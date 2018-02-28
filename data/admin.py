from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Address)
admin.site.register(PersonalInfo)
admin.site.register(WorkInfo)
admin.site.register(Insignia)
admin.site.register(Education)
admin.site.register(NewsInHome2)
