from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
import random
from django.core.mail import send_mail
from django.conf import settings
import pytz
import datetime
from datetime import timedelta

timezone = pytz.timezone('UTC')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp_email(self, email, otp):
        subject = 'OTP for Login'
        message = f'Your OTP is: {otp}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

    def send_otp_sms(self, phone_number, otp):
        # Code to send OTP via SMS
        pass

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def send_otp(self):
        otp = CustomUserManager().generate_otp()
        self.otp = otp
        self.otp_created_at = datetime.datetime.now(timezone)
        self.save()

        CustomUserManager().send_otp_email(self.email, otp)

    def verify_otp(self, otp):
        if self.otp == otp and self.otp_created_at >= datetime.datetime.now(timezone) - timedelta(minutes=5):
            self.otp = otp
            self.otp_created_at = datetime.datetime.now(timezone)
            self.save()
            return True
        return False
    

class City(models.Model):
    name = models.CharField(max_length=35)
    country_code = models.CharField(max_length=3)
    district = models.CharField(max_length=20)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=52)
    continent = models.CharField(max_length=50)
    region = models.CharField(max_length=26)
    surface_area = models.CharField()
    indep_year = models.CharField(null=True, blank=True)
    population = models.CharField()
    life_expectancy = models.CharField(null=True, blank=True)
    gnp = models.CharField(null=True, blank=True)
    gnp_old = models.CharField(null=True, blank=True)
    local_name = models.CharField(max_length=45)
    government_form = models.CharField(max_length=45)
    head_of_state = models.CharField(max_length=60, null=True, blank=True)
    capital = models.CharField(null=True, blank=True)
    code2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
class CountryLanguage(models.Model):
    country_code = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    is_official = models.CharField()
    percentage = models.CharField()

    def __str__(self):
        return self.language