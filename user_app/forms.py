from django import forms

from user_app.models import CustomUser

class UserregistrationForm(forms.ModelForm):

    class Meta:

         model = CustomUser

         fields = ['username','mobile_number','email','password']