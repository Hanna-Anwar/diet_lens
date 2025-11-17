from django.db.models.signals import post_save

from django.dispatch import receiver

from user_app.models import CustomUser 

from django.core.mail import send_mail

@receiver(post_save,sender=CustomUser)
def send_register_mail(sender,instance,created,**kwargs):

    if created:

        subject = "Hello from dietlens"

        message = "Welcome to dietLens"

        from_email = "23mca38@mgits.ac.in"

        recipient_list = [instance.email]

        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
         
        print("mail sent")







