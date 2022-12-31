from django.contrib import admin
from .models import patient

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['name','description','city']

admin.site.register(patient,userAdmin)
