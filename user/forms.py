from django import forms
from user.models import MyUser
from django.forms import ModelForm

class RegisterForm(ModelForm):
    model = MyUser
    fields=[
        'username','email','password','phone','country','city','date_of_birth','profile_pic','first_name','last_name'
    ]
    widgets={
        'password':forms.PasswordInput(),
        'username':forms.TextInput(),
        'email':forms.EmailField(),
        'phone':forms.TextInput(),
        'country':forms.TextInput(),
        'city':forms.TextInput(),
        'date_of_birth':forms.DateField(),
        'profile_pic':forms.FileField(),
        'first_name':forms.TextInput(),
        'last_name':forms.TextInput(),

       
    }