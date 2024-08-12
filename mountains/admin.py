from django.contrib import admin
from mountains.models import Mountain

class MountainAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mountain, MountainAdmin)
