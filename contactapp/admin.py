from django.contrib import admin
from contactapp.models import contactNum
class contactfont(admin.ModelAdmin):
    list_display = ('firstname','lestname','email','password','number','description','con_image')
    
admin.site.register(contactNum,contactfont)   
# Register your models here.
