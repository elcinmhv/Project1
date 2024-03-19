from django.forms import ModelForm
from django import forms
from core.models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        model=ContactUs
        fields=['message','name','email','subject']


        widgets={
            'message':forms.Textarea(attrs={'placeholder':'Enter Message' ,'class':'form-control w-100', 'name':'message', 'id':'message', 'cols':'30', 'rows':'9'}),
            'name':forms.TextInput(attrs={'placeholder':'Enter your name' ,'class':'form-control ','name':'name', 'id':'name' ,'type':'text',}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email address', 'class':'form-control ', 'name':'email', 'id':'email' ,'type':'email'}),
            'subject':forms.TextInput(attrs={'placeholder':'Enter Subject','class':"form-control ", 'name':"subject", 'id':"subject",'type':'text'})
        }