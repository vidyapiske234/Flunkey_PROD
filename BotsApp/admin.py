from django.contrib import admin
from BotsApp.models import Bot

# Register your models here.

class BotAdmin(admin.ModelAdmin):
    list_display = ['id','bot_name', 'bot_no', 'bot_color', 'rest']
    list_per_page = 50


admin.site.register(Bot, BotAdmin)