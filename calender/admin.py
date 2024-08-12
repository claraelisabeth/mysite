from django.contrib import admin
from calender.models import Subject, Freetime

class CalenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, CalenderAdmin)
admin.site.register(Freetime, CalenderAdmin)