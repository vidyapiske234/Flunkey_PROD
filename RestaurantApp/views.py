from django.shortcuts import redirect, render
from RestaurantApp.models import Delivery, Restaurant, Table, TempDelivery
import time
# Create your views here.


#......   SHOWING RESTAURANTS   ...................................................................
def RestListView(request):    
    r = Restaurant.objects.all()
    return render(request, 'rest_list.html', {'r':r})
#..................................................................................................


#......   SHOWING TABLES   ........................................................................
def TableListView(request):
    return render(request, 'RestaurantApp/tables_list.html')    
#..................................................................................................


#......   SELECTING TABLE   .......................................................................
def SelectTableView(request, id):
    #... Fetching delected table details.....
    table =  Table.objects.get(id = id)

    #... Fetch the recent temp object of the rest.....
    t = TempDelivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')

    #... updating the table details in TempDelivery object.....
    t.table_no = table.table_no
    t.save()
    return redirect('RestaurantApp:confirm-delivery')
#..................................................................................................


#... Confirm DElivery details .....................................................................
def ConfirmDetailsVIew(request):
    t = TempDelivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')

    if request.method == "POST":
        FD = Delivery.objects.create(
                                       username = t.username,
                                       restaurant = t.restaurant,
                                       bot_id = t.bot_id,
                                       bot_name = t.bot_name,
                                       bot_color = t.bot_color,
                                       table_no = t.table_no,
                                       port = t.port,
                                       ip = t.ip,
                                       time = time.time()
                                    )
        FD.save()
        t.delete()
        return redirect('RestaurantApp:delivery-details')
    return render(request, 'RestaurantApp/confirm_delivery.html' ,{'t':t})
#..................................................................................................


#... Delivery details .............................................................................
def DeliveryDetailView(request):
    d = Delivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')
    return render(request, 'RestaurantApp/delivery_details.html', {'d':d})
#..................................................................................................


#... End deliveries today .........................................................................
def EndTodayView(request):
    d = Delivery.objects.latest('pk')
    d.time = 0
    d.save()

    return redirect('BotsApp:bots-list')
#..................................................................................................