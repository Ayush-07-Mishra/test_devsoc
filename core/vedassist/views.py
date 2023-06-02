from django.shortcuts import render , redirect
from .models import*
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from .predictor import model_predict


def home(request):
    return render(request , 'home.html')
    
    
@login_required(login_url="/login/")
def test(request):
    user = request.user
    return render(request, 'test.html', {'user': user})


@login_required(login_url="/login/")
def result(request):
    return render(request, 'result.html')


def predict(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        
        age = request.POST.get('age')
        if not age:
            return HttpResponseRedirect(reverse("test"))
        
        weight = request.POST.get('weight')
        if not weight:
            return HttpResponseRedirect(reverse("test"))
            
        user_input = [
            0 if request.POST.get('cold') == 'yes' else 1,
            0 if request.POST.get('eyepain') == 'yes' else 1,
            0 if request.POST.get('fever') == 'yes' else 1,
            0 if request.POST.get('headache') == 'yes' else 1,
            0 if request.POST.get('stomachache') == 'yes' else 1,
            0 if request.POST.get('dizziness') == 'yes' else 1,
            0 if request.POST.get('vomiting') == 'yes' else 1,
            0 if request.POST.get('chestpain') == 'yes' else 1,
            0 if request.POST.get('jointpain') == 'yes' else 1,
            0 if request.POST.get('loosemotion') == 'yes' else 1,
            0 if request.POST.get('throatinfection') == 'yes' else 1,
            int(request.POST.get('age')),
            int(request.POST.get('gender')),
            int(request.POST.get('weight'))
        ]
        
        medicines = model_predict(str(user_input).lstrip('[').rstrip(']'))
        print(medicines)
        
        # predictor here
        context = {
            'medicine1': medicines[0][0],
            'medicine2': medicines[0][1],
            'medicine3': medicines[0][2],
        }

        return render(request, 'result.html', context)
        
    else:
        return HttpResponseRedirect(reverse("test"))



def login_page(request):
    if request.method == "POST":
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
            return redirect('/test/')


    return render(request, 'login.html')



def logout_page(request):
    logout(request)
    return redirect('/login')


def register(request):



    if request.method != "POST":
        return render(request, 'register.html')
    


    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')




    user = User.objects.filter(username=username)


    if user.exists():
        messages.info(request, "Username Already Exists")
        return redirect('/register/')


    user = User.objects.create(
        first_name= first_name, 
        last_name= last_name,
        username=username,
        # password=password  we cant directly add password so we have encrypt it
        )

    user.set_password(password)    # this method is already thier in django
    user.save()
    messages.info(request, "Account created successfully")

    return redirect('/login/')






























