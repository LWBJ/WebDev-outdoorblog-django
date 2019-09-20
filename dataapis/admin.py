from django.contrib import admin
from dataapis.models import OutdoorDate
# Register your models here.

class OutdoorDateAdmin(admin.ModelAdmin):
  list_display = ('title', 'place', 'date')
  

admin.site.register(OutdoorDate, OutdoorDateAdmin)