from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from BotsApp.models import Bot
from RestaurantApp.models import TempDelivery

# Create your views here.
def BotListView(request):
    return render(request, 'BotsApp/bots_list.html')

def SelectBotView(request, id):
    #.... fetching objects......
    b = Bot.objects.get(id = id)
    user = request.user.username
    rest = request.user.rest

    #... Creating Temp delivery.....
    t = TempDelivery.objects.create(
                                     username = user,
                                     restaurant = rest.rest_name,
                                     bot_name = b.bot_name,
                                     bot_id = b.id,
                                     bot_color = b.bot_color,
                                     ip = b.ip,
                                     port = b.port,                                      
                                    )
    t.save()

    return redirect('RestaurantApp:table-list')

