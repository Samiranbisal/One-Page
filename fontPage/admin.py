from django.contrib import admin
from fontPage.models import fontpage
class font(admin.ModelAdmin):
    list_display = ('name','title','description')
    
admin.site.register(fontpage,font)    
# Register your models here.
