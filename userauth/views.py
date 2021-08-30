from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(useremail=email, pasword=password)
        if user is not None:
            auth.login(request,user)
            print("login success")
            return redirect('/')
        else:
            messages.error(request ,"invalid Username or Password")
            print("login Failed")
            return redirect('login')
    else:
        return render(request, 'userauth/login.html')
        

# def logout(request):
#     if request.method == 'POST':
#         loguser = request.POST.get('logemail')
#         logpass = request.POST.get('logpassword')
#         user = authenticate(username=loguser, pasword=logpass)
#         if user is not None:
#             login(login,user)
#             messages.success(request, "login Success")
#             return redirect('/')
#         else:
#             messages.error( request ,"invalid Username or Password")            
#     return redirect('/')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        userpass = request.POST.get('password')
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
        crt_user = User.objects.create_user(username=username, email=useremail, password=userpass)
        crt_user.save()
        print("user created")
        return redirect('/')
        
    else:
        return render(request, 'userauth/signup.html')
