from django import forms

from user_app.models import CustomUser

class UserregistrationForm(forms.ModelForm):

    class Meta:

         model = CustomUser

         fields = ['username','mobile_number','email','password']

class ForgotemailForm(forms.Form): 
     
     email = forms.CharField(max_length=30)

     #used form insteadof Modelform because their is no model

class OtpverifyForm(forms.Form):
     
     otp = forms.CharField(max_length=10)