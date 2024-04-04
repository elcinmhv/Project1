from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .forms import RegisterForm,LoginForm
# Create your views here.



def register(request):
    context = {

        'title': 'Register',

        'form': RegisterForm

    }

    if request.method == 'POST':

        if request.POST['password'] != request.POST['confirm_password'] :

            context['error'] = 'Passwords do not match'

            return render(request, 'register.html', context)
        

        else:

            form = RegisterForm(request.POST, request.FILES)

            if form.is_valid():

                user = form.save(commit=False)

                user.set_password(user.password)

                user.save()

                return redirect('login')

    return render(request, 'register.html', context)



def login(request):
    context={
        'forms':LoginForm()
    }
    if request.method=='POST':
        alma=authenticate(username=request.POST['username'],password=request.POST['password'])
        if alma:
            auth_login(request,alma)
            return redirect('index')
        else:
            context['error']='Invalid Username or Password'
    
    return render(request,'login.html',context)



def logout(request):
    auth_logout(request)
    return redirect('login')
           