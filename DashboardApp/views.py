from django.http.response import HttpResponse
from django.shortcuts import render
from RestaurantApp.models import Delivery
from BotsApp.models import Bot
from datetime import date, datetime

# Create your views here.

def DashboardView(request):
    return render(request, 'DashboardApp/dashboard.html')

def BotDashboardView(request, id):
    if request.method == "POST":
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        bot = Bot.objects.get(id = id)



        fd = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name)
        td = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name,created_at__date = date.today())
        date1 = datetime.today()
        week = date1.strftime('%V')
        tw = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name,created_at__week = week)

        if enddate > startdate:
            print(startdate, enddate)
            d_post = Delivery.objects.filter(created_at__range=(startdate, enddate), bot_name = bot.bot_name)
            print(d_post)
            return render(request, 'dashboardApp/bot_dashboard.html', {
                                                                        'd_post':len(d_post),
                                                                        'fd':len(fd),
                                                                        'td':len(td),
                                                                        'bot_name':bot.bot_name, 
                                                                        'bot':bot,  
                                                                        'tw':len(tw),
                                                                        'startdate': startdate,
                                                                        'enddate':enddate,
                                                                    })
        else:
            return HttpResponse('Invlaid dates submitted')

    else:
        bot = Bot.objects.get(id = id)

        fd = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name)

        td = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name,created_at__date = date.today())

        date1 = datetime.today()
        week = date1.strftime('%V')

        tw = Delivery.objects.filter(food_delivered = False, bot_name = bot.bot_name,created_at__week = week)

        return render(request, 'dashboardApp/bot_dashboard.html', {
                                                                'fd':len(fd),
                                                                'td':len(td),
                                                                'bot_name':bot.bot_name, 
                                                                'bot':bot,  
                                                                'tw':len(tw),
                                                                })