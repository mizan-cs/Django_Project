from django.db import models
from applicant.models import Applicant
# Create your models here.
class student(models.Model):
    pass

class applicent(Applicant):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name