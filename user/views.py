from django.shortcuts import render
from user.forms import RegisterForm

# Create your views here.


def register(request):
    form=RegisterForm
    context={
        'form':form
    }
    return render(request,'register.html',context=context)