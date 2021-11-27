from RestaurantApp.models import Restaurant, Table, Delivery
from BotsApp.models import Bot
from AccountsApp.models import CustomUser as User
from datetime import date, datetime 

def rest_data(request): 
    try:
        rest = request.user.rest
        bots = Bot.objects.filter(rest = request.user.rest, avialable = True)
        table = Table.objects.filter(rest = request.user.rest, avialable = True)

        nbots = Bot.objects.filter(rest = request.user.rest, avialable = False)
        ntable = Table.objects.filter(rest = request.user.rest, avialable = False)

        fd = Delivery.objects.filter(food_delivered = False)
        td = Delivery.objects.filter(created_at__date = date.today(), food_delivered = True) 

        ab = Bot.objects.filter(rest = request.user.rest, status = True)
        at = Table.objects.filter(rest = request.user.rest, avialable = True)

        ab1 = Bot.objects.filter(rest = request.user.rest, status = True)


    except:
        bots = []
        table = []
        rest = ''
        nbots = []
        ntable = []

        fd = []
        td = []

        ab = []
        at = []
        ab1 = []

    return {'rest':rest, 
            'bots':bots, 
            'table':table, 
            'nbots':nbots, 
            'ntable':ntable,
            'fd':len(fd),
            'td':len(td),
            'ab':len(ab),
            'at':len(at),
            'ab1':ab1,
            }