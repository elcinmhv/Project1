from django.shortcuts import redirect, render
from user.forms import RegisterForm

# Create your views here.


def register(request):
    form=RegisterForm()
    # if request.METHOD=='POST':
    #     form=RegisterForm(request.POST)

    context={
        'form':form
    }
    return render(request,'register.html',context=context)
    # context = {

    #     'title': 'Register',

    #     'form': RegisterForm()

    # }

    # if request.method == 'POST':

    #     if request.POST['password'] != request.POST['confirm_password']:

    #         context['error'] = 'Passwords do not match'

    #         return render(request, 'register.html', context  )       
    #     else:

    #         form = RegisterForm(request.POST, request.FILES)

    #         if form.is_valid():

    #             user = form.save()

    #             user.set_password(user.password)

    #             user.save()

    #             return redirect('index')

    # return render(request, 'register.html', context)