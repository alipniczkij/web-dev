from django.contrib import admin
from .models import Machine, Driver, Order


class MachineAdmin(admin.ModelAdmin):
    list_display = ('brand', 'level', 'numbers', 'color', 'release_year')
    list_display_links = ('numbers',)
    search_fields = ('brand', 'level', 'numbers', 'release_year')

class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'birthday', 'machine', 'inn', 'passport') 
    list_display_links = ('name',)
    search_fields = ('name', 'surname', 'patronymic', 'birthday', 'machine', 'inn', 'passport')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('driver', 'address_from', 'address_to', 'route_length', 'passengers_num', 'created_at')
    search_fields = ('address_from', 'address_to', 'created_at', 'driver')

admin.site.register(Machine, MachineAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Order, OrderAdmin)
 