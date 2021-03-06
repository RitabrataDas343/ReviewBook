from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from movies.models import Movie, MovieFollow
from django.conf import settings

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an unique username")
        if not first_name:
            raise ValueError("Users must enter First Name")
        if not last_name:
            raise ValueError("Users must enter Last Name")

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                followercount=0,
                followingcount=0,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
                email=self.normalize_email(email),
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email =        models.EmailField(verbose_name="EmailId", max_length=100, unique=True)
    username =     models.CharField(max_length=40, unique=True)
    date_joined =  models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login =   models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin =     models.BooleanField(default=False)
    is_active =    models.BooleanField(default=True)
    is_staff =     models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name =   models.CharField(max_length=100)
    last_name =    models.CharField(max_length=100)
    dob =          models.DateField(null=True)
    following = models.ManyToManyField("self", symmetrical=False)
    followercount = models.IntegerField(blank=True, null=True)
    followingcount = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True
