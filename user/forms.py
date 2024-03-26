from django import forms
from user.models import MyUser

class RegisterForm(forms.ModelForm):
    model=MyUser
    fields=[
        'username','email','password','phone','country','city','date_of_birth','profile_pic'
    ]
    widgets={
        'password':forms.PasswordInput(),
    }