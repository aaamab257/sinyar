from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib.auth.models import Permission ,PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, email ,  name ,phone, is_admin,is_vendor,fcm_token , is_user ,  password=None,password2=None,date_of_birth=None  ):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name= name,
            phone = phone,
            date_of_birth = date_of_birth,
            is_admin = is_admin,
            is_user = is_user,
            is_vendor = is_vendor,
            fcm_token = fcm_token
            
        )
        user.is_user = is_user 
        user.is_vendor = is_vendor 
        user.phone = phone
        user.fcm_token =fcm_token
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone,is_admin ,is_user,is_vendor ,fcm_token ,  name , password=None ):
        
        user = self.create_user(
            email,
            name = name,
            password=password,
            is_user = is_user,
            is_vendor = is_vendor,
            fcm_token = fcm_token,
            phone=phone,
            is_admin=is_admin
        )
        user.phone = phone
        user.name = name
        user.fcm_token =fcm_token
        user.is_user = False 
        user.is_vendor = False 
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    phone = models.CharField( max_length=20, unique=True,)
    date_of_birth = models.CharField(max_length=55,null=True,blank=False)
    is_vendor=  models.BooleanField(default=False , null=True)
    is_user = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fcm_token = models.CharField(_("FCM Token"), max_length=200, null=True, blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name','email' , 'is_admin' , 'fcm_token']

    def __str__(self):
        return "{}".format(self.email)

    def has_perm(self, perm, obj=None):
        
        return self.is_admin

    def has_module_perms(self, app_label):
        
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('User')