from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
)
from .model_fields import (
    LowercaseEmailField
)
# Create your models here

class MySystemUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class ClientModel(AbstractBaseUser):
    id                  = models.AutoField(primary_key=True)
    email               = LowercaseEmailField(verbose_name="Email",unique=True) #models.EmailField(verbose_name="email", max_length=60, unique=True)
    system_id           = models.IntegerField(default=1)
    username            = models.CharField(max_length=60)
    firstname           = models.CharField(blank=True,null=True,max_length=30)
    lastname            = models.CharField(blank=True,null=True,max_length=30) 
    created_at          = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at          = models.DateTimeField(verbose_name="updated at", auto_now=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    email_verified      = models.BooleanField(default=False)
    is_enabled          = models.BooleanField(default=False)
    objects             = MySystemUserManager()
    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS     = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def email_user(self, *args, **kwargs):
        send_mail(
            '{}'.format(args[0]),
            '{}'.format(args[1]),
            None,
            [self.email],
            fail_silently=False,
        )
