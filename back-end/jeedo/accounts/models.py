from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch
from django.db.models.signals import pre_save, post_delete
import random
from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.apps import apps

# Create your models here.
class AspirantProfile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE),
    dob = models.DateField(),
    phone = models.CharField(max_length=12),
    profile_image = models.ImageField(default='default.jpg',upload_to='aspirant_images')

    def student_register_email(self):
        from_email = settings.JEEDO_EMAIL
        with get_connection(
            username =from_email,
            password = settings.JEEDO_EMAIL_PASSWORD
        ) as connection :
            subject = "Registered with JeeDo"
            to_email = [self.user.email]
            html_content = render_to_strings('accounts/student_register_email.html',
                    {'username': self.user.username, 'email' : self.user.email})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject=subject,body = text_content,from_email=from_email,
                        to=to_email,connection=connection)
            message.attach_alternative(html_content,'text/html')
            message.send()  


    def __str__(self):
        return self.user.get_full_name()


class ExpertProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE),
    educ_qual = models.Text_Field(max_length=250)
    presently_working= models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    dob = models.DateField()
    is_verified= models.BooleanField(default = False)
    linkedin_profile = models.CharField(required = False,max_length= 100)
    profile_image = models.ImageField(default='default.jpg',upload_to= 'expert_images')


    def __str__(self):
        return self.user.get_full_name()

    def expert_register_email(self):
        from_email = settings.JEEDO_EMAIL
        with get_connection(
            username =from_email,
            password = settings.JEEDO_EMAIL_PASSWORD
        ) as connection :
            subject = "Registered with JeeDo"
            to_email = [self.user.email]
            html_content = render_to_strings('accounts/expert_register_email.html',
                    {'username': self.user.username, 'email' : self.user.email})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject=subject,body = text_content,from_email=from_email,
                        to=to_email,connection=connection)
            message.attach_alternative(html_content,'text/html')
            message.send()    




        



