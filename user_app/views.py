from django.shortcuts import render,redirect

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from user_app.forms import UserregistrationForm,ForgotemailForm,OtpverifyForm

from user_app.models import CustomUser

from django.core.mail import send_mail

import random

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
    
class ForgotemailView(View):

    def get(self,request):

        form  = ForgotemailForm()

        return render(request,"forget.html",{"form":form})
    
    def post(self,request):

        email = request.POST.get('email')

        user = CustomUser.objects.get(email=email)

        if user:

            otp_generate = random.randint(1000,9999)

            request.session['otp'] = otp_generate

            request.session['email'] = email

            send_mail(subject = "forget password",
                      message = str(otp_generate),
                      from_email="23mca38@mgits.ac.in",
                      recipient_list = [email])
             
            print("done")

        return render(request,"forget.html")
    
class OtpVerifyView(View):

    def get(self,request):

        form = OtpverifyForm()

        return render(request,"otpverify.html",{"form":form})
  
