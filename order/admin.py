from django.contrib import admin
from .models import Order 
# Register your models here.
admin.site.register(Order)

admin.site.site_header = 'Alia Bakery Shop Administration'           
admin.site.index_title = 'Orders Area'                 
admin.site.site_title = 'Alia Bakery Shop Administration' 