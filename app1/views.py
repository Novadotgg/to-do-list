from django.shortcuts import render, HttpResponse,redirect
# from django.views.decorators.csrf import csrf_protect
# from django.http import HttpResponseForbidden
# from django.template import loader

# def csrf_failure(request, reason=''):
#     template = loader.get_template('csrf_failure.html')
#     return HttpResponseForbidden(template.render())
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import login_required
# @login_required(login_url='log')

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cf=request.POST.get('confirm') 
        if password!=cf:
            return HttpResponse("Passwords don't match")
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')
    return render(request, 'logreg.html')
    
        

def LoginPage(request):
    if request.method == 'POST':
        usernam = request.POST.get('un')
        pas = request.POST.get('pass')
        user = authenticate(request, username=usernam, password=pas)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Incorrect Credentials")
    return render(request, 'logreg.html')



def Logout(request):
    logout(request)
    return redirect('signup')
    # return render(request,'home.html')




# def LoginPage(request):
#     if request.method == 'POST':
#         usernam = request.POST.get('un')
#         pas = request.POST.get('pass')
#         print(usernam,pas)
#         # user = authenticate(request, username=usernam, password=pas)
#         # if user is not None:
#         #     login(request, user)
#         #     return HttpResponse("You are logged in successfully")
#         # else:
#         #     return HttpResponse("Login failed. Please check your credentials.")
#     return render(request, 'logreg.html')
