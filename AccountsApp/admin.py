from django.contrib import admin

# Register your models here.
from .models import CustomUser as User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'rest', 'email']
admin.site.register(User, UserAdmin)