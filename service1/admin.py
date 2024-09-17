from django.contrib import admin

from service1.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('Book_icon', 'Book_title', 'Book_des')
    
admin.site.register(Book,BookAdmin)    

# Register your models here.
