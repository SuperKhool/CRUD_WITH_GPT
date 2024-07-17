from django.contrib import admin
from .models import Employ
# Register your models here.

class EmployAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')

    
admin.site.register(Employ,EmployAdmin)
