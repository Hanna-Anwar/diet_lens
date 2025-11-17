from django import forms

from user_app.models import CustomUser

class UserregistrationForm(forms.ModelForm):

    class Meta:

         model = CustomUser

         fields = ['username','mobile_number','email','password']

         #its a dictionery
         #textInput is a method

         widgets = {
              
              "username": forms.TextInput(attrs={
                   
                   "class":"form-control",
                   "placeholder":"enter your username"
                   
              }),

              "mobile_number":forms.TextInput(attrs={
                    "class":"form-control",
                   "placeholder":"enter your mobile_no"
              }),
              
              "email":forms.EmailInput(attrs={
                   
                    "class":"form-control",
                   "placeholder":"enter your email"
                   
              }),

              "password":forms.PasswordInput(attrs={
                   "class":"form-control",
                   "placeholder":"enter your password"

              })

              
         }


class ForgotemailForm(forms.Form): 
     
     email = forms.CharField(max_length=30)

     #used form instead of Modelform because their is no model



class OtpverifyForm(forms.Form):
     
     otp = forms.CharField(max_length=10)

     

class ResetPasswordForm(forms.Form):

     new_password = forms.CharField(max_length=20)

     confirm_password = forms.CharField(max_length=20)