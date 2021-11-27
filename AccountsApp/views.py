from django.http.request import HttpHeaders
from django.shortcuts import render, redirect, reverse  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from RestaurantApp.models import Restaurant, Table
from BotsApp.models import Bot

# Create your views here.


# LOGIN VIEW..................................................................
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('BotsApp:bots-list')
        else:
            return HttpResponse("wrong creds entered")
    else:
        return render(request, 'AccountsApp/login.html')
#...............................................................................

def SignupView(request):
    if request.method == "POST":
        #user = .....
        #user.save.....
        pass
    else:
        # form
        # redirection
        pass



@login_required
def LogoutView(request):
    logout(request)
    return redirect('AccountsApp:login')    