from django.shortcuts import render,redirect

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from user_app.forms import UserregistrationForm

from user_app.models import CustomUser

from django.core.mail import send_mail

class RegistrationView(View):

    def get(self,request):

        form =  UserregistrationForm()

        return render(request,"registration.html",{"form":form})
    

    def post(self,request):

        form = UserregistrationForm(request.POST)

        if form.is_valid():

            

    #def post(self,request):
    # 
    #   print(request.POST)
    # 
    #   form = UserregisterForm(request.POST)
    #   
    #   if form.is_valid():
    # 
    #       print(form.cleaned_data)
    #       CustomUser.objects.create_user(username = form.cleaned_data.get("username"),
    #                                      email = form.clened_data.get("email"),
    #                                      mobile_number = form.cleaned_data.get("mobile_number"),
    #                                      password = form.cleaned_data.get("password"))
    # 
    #       return render(request,"signup.html")
    #   return render(request,"signup.html")
            

            CustomUser.objects.create_user(username= form.cleaned_data.get('username'),
                                          mobile_number = form.cleaned_data.get('mobile_number'),
                                          email = form.cleaned_data.get('email'),
                                          password = form.cleaned_data.get('password'))
         
            form = UserregistrationForm()
        
            return render(request,"registration.html",{"form":form})
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
  




  