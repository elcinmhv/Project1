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


# from django import forms
# from .models import ContactUs

# class ContactUsForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ContactUsForm, self).__init__(*args, **kwargs)
#         self.fields['subject'].widget = forms.Select(attrs={'class': 'form-control'}, choices=self.get_subject_choices())

#     def get_subject_choices(self):
#         # Burada subject için seçenekleri dinamik olarak oluşturmalısınız
#         # Örneğin, bir veritabanından çekebilirsiniz
#         # Bu sadece bir örnektir, gerçek kodunuz veri modelinize ve gereksinimlerinize göre değişecektir
#         return [
#             ('general', 'General Inquiry'),
#             ('support', 'Customer Support'),
#             ('feedback', 'Feedback'),
#         ]   
    
    

#     class Meta:
#         model = ContactUs
#         fields = ['message', 'name', 'email', 'subject']

#         widgets = {
#             'message': forms.Textarea(attrs={'placeholder': 'Enter Message', 'class': 'form-control w-100', 'name': 'message', 'id': 'message', 'cols': '30', 'rows': '9'}),
#             'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control', 'name': 'name', 'id': 'name', 'type': 'text'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter email address', 'class': 'form-control', 'name': 'email', 'id': 'email', 'type': 'email'}),
#             'subject': forms.Select(attrs={'placeholder': 'Enter Subject', 'class': "form-control", 'name': "subject", 'id': "subject"})
#         }
