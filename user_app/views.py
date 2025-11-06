from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from user_app.forms import UserregistrationForm

from user_app.models import CustomUser

class RegistrationView(View):

    def get(self,request):

        form =  UserregistrationForm()

        return render(request,"registration.html",{"form":form})
    

    def post(self,request):

        print(request.POST)

        CustomUser.objects.create_user(username= request.POST.get('username'),
                                       mobile_number = request.POST.get('mobile_number'),
                                        email = request.POST.get('email'),
                                        password = request.POST.get('password') )
        
        form = UserregistrationForm()
        
        return render(request,"registration.html",{"form":form})
    

class  LoginView(View):

    def get(self,request):

        return render(request,"login.html")
    
    def post(self,request):

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:

            login(request,user)

            return render(request,"registration.html")

        return redirect("login")       

class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("login")
        


