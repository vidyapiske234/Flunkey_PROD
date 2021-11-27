from django.urls import path
from . import views

app_name = 'BotsApp'

urlpatterns = [
    path('', views.BotListView, name = 'bots-list'),
    path('<str:id>', views.SelectBotView, name = 'select-bot'),
]
