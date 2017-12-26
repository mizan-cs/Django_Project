from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class Base_Applicant(BaseUserManager):
    def _create_applicant(self,email,password,is_staff,is_superuser,**extra_fields):

        '''create and save a applicant with the given email and password'''
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        applicant = self.model(email=email,is_staff=is_staff,
                               is_active=True,is_superuser=is_superuser,
                               last_login = now,date_joined = now, **extra_fields)
        applicant.set_password(password)
        applicant.seve(using=self.db)
        return applicant

    def create_applicant(self,email,password=None,**extra_fields):
        return self._create_applicant(email,password,False,False,**extra_fields)

    def create_super_applicant(self, email, password=None, **extra_fields):
        return self._create_applicant ( email, password, True, True, **extra_fields )




class Applicant(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    full_name = models.CharField(max_length=254,blank=True)
    email = models.EmailField(blank=True,unique=True)
    mobile_number = models.CharField(max_length=20)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','full_name','email','mobile_number']

    objects = Base_Applicant()
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_mobile_number(self):
        return self.mobile_number

    def get_name(self):
        return self.full_name

    def sent_mail_to_applicant(self,subject,message,from_email=None):
        send_mail(subject,message,from_email,[self.email])





