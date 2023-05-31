from django.shortcuts import render , redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def login_page(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Inavlid Username")
            return redirect('/login/')
        
        user =authenticate(username = username, password = password)

        if user is None:    
            messages.info(request, "Inavlid Password")
            return redirect('/login/')
        
        else:
            login(request,user)       # iska name(lgoin()) aur function ka name (login_page) diffrent hona chaiye 
                        # varna infiniite loop chlenga 
            return redirect('/receipes/')


    return render(request, 'login.html')


