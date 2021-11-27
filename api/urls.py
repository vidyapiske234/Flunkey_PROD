from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('all-deliveries/', views.AllDeliveriesView, name = 'all-deliveries'),
    path('latest-delivery/', views.LatestDeliveryView, name = 'latest-delivery'),
    path('bot-status/<str:id>', views.BotStatusView, name = 'bot-status-update'),
    path('bot-battery/<str:id>', views.BotBatteryView, name = 'bot-battery'),
    path('table-status/<str:id>', views.TableStatusView, name = 'table-status'),    
    path('delivery-status/<str:id>', views.DeliveryStatusView, name = 'delivery-status'),
    path('<str:username>/latest', views.RestLatestView, name = 'rest-latest')
]
