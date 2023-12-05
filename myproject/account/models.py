from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True,verbose_name="ایمیل")
    is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
    spetial_user =  models.DateTimeField(default=timezone.now,verbose_name="کاربر خصوصی تا")
    
    def is_spetial_user(self):
        if self.spetial_user > timezone.now():
            return True
        else:
            return False
        
    is_spetial_user.boolean=True 
    is_spetial_user.short_description="وضعیت کاربر خصوصی"
       
        
        
    
    