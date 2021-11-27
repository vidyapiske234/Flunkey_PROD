from django.urls import path
from . import views
app_name = 'DashboardApp'

urlpatterns = [
    path('', views.DashboardView, name = 'dashboard'),
    path('bot/<str:id>', views.BotDashboardView, name = 'bot-dashboard')
]
