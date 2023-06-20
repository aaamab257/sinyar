from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib.auth.models import Permission ,PermissionsMixin
# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, email ,  name ,phone, is_admin, password=None,password2=None,date_of_birth=None  ):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
            name= name,
            phone = phone,
            date_of_birth = date_of_birth,
            is_admin = is_admin,
            
        )
        user.phone = phone
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone,is_admin ,  name , password=None ):
        
        user = self.create_user(
            email,
            name = name,
            password=password,
            
            phone=phone,
            is_admin=is_admin
        )
        user.phone = phone
        user.name = name
        
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
    phone = models.BigIntegerField()
    date_of_birth = models.CharField(max_length=55,null=True,blank=False)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone' , 'is_admin']

    def __str__(self):
        return "{}".format(self.email)

    def has_perm(self, perm, obj=None):
        
        return self.is_admin

    def has_module_perms(self, app_label):
        
        return True

    

    @property
    def is_staff(self):
        
        return self.is_admin