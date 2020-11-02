from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HomeTeam(models.Model):
    POSITION=(
        ('Web-Developer','Web-Developer'),
        ('Maintainer','Maintainer'),
        ('Mentor','Mentor')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=200,blank=True)
    role = models.CharField(max_length=20,choices = POSITION)
    profile_image= models.ImageField(default = 'default.png',upload_to='member_image')

    def __str__(self):
        return self.member.user.get_full_name()