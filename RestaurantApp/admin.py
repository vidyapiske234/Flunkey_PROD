from django.contrib import admin
from .models import Restaurant, Table, TempDelivery, Delivery

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_no', 'rest']

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant', 'bot_name', 'bot_id', 'bot_color', 'table_no', 'time']
    list_per_page =  500

admin.site.register(Restaurant)
admin.site.register(Table, TableAdmin)
admin.site.register(TempDelivery)
admin.site.register(Delivery, DeliveryAdmin)
