from django import forms

from diet_advisor_app.models import UserProfileModel

class  UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfileModel

        fields = ['age','gender','height','weight','goal']
        