from django import forms
from .models import MyUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=['username','first_name','last_name','email','phone','country','city','date_of_birth','profile_pic','password',]
        widgets={
            'password' : forms.PasswordInput(),
            'date_of_birth' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'profile_pic' : forms.FileInput(),
            'email':forms.TextInput(attrs={'placeholder':'Enter email address', 'class':'form-control ', 'name':'email', 'id':'email' ,'type':'email'})
        }

    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password does not match')
        return cleaned_data
    



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name' ,'class':'form-control ','name':'name', 'id':'name' ,'type':'text',}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password' ,'class':'form-control ','name':'password', 'id':'password' ,}))