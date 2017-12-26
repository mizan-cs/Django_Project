from django.shortcuts import render,HttpResponse
from .form import Reg_Form
from django import forms
# Create your views here.
def sing_up(request):

    return render(request,'page/singup.html')

