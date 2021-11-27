from django.contrib import admin
from .models import Restaurant, Table, TempDelivery, Delivery

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_no', 'rest']

admin.site.register(Restaurant)
admin.site.register(Table, TableAdmin)
admin.site.register(TempDelivery)
admin.site.register(Delivery)