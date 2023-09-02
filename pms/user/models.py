from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

genderChoice=(
   ("Male","male"),
   ("Female","female"),
   ("Other","other")
)

class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_manager =  models.BooleanField(default=False)
    is_team_leader = models.BooleanField(default=False)
    is_tester = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True, null=False)
    gender = models.CharField(choices=genderChoice, default=True, max_length=100)
    profile_pic =models.ImageField(upload_to='images/',null=True,blank=True)

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

    
    def __str__(self):
        return self.username 