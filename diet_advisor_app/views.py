from django.shortcuts import render

from diet_advisor_app.models import UserProfileModel

from diet_advisor_app.forms import UserProfileForm

from django.views.generic import View

class CreateProfileView(View):

    def get(self,request):

        form = UserProfileForm()

        return render(request,"profile.html",{"form":form})
