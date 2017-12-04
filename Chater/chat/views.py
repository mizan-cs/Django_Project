from django.shortcuts import render, redirect
from chat.models import user_data, Conversation, Person
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Conversation,Person
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .dataset import conversation

from .forms import UserForms

# ----------------------------------
doctor = ChatBot ( "Doctor")
doctor.set_trainer ( ListTrainer )
doctor.train ( conversation )



def home_view(request):
    if request.user.is_authenticated ():

        if request.method == 'POST':
            doctor_p = Conversation()
            man = Conversation()

            man.massage = request.POST.get('massage')
            man.type_id = 1

            doctor_p.massage = doctor.get_response(request.POST.get('massage'))
            doctor_p.type_id = 2

            man.save()
            doctor_p.save()

        context = Conversation.objects.all()

        return render ( request, 'design/chater.html', {'conversations': context} )
    else:
        return redirect ( 'login_views' )


def login_view(request):
    if request.method == 'POST':
        user = authenticate ( username=request.POST.get ( 'username' ), password=request.POST.get ( 'password' ) )
        if user:
            if user.is_active:
                login ( request, user )
                return redirect ( 'HomePage' )
            else:
                return HttpResponse ( 'User is Disable' )
        else:
            return render ( request, 'design/login_page.html', {'massage': 'username or password is invalid'} )

    return render ( request, 'design/login_page.html' )


def registration_view(request):
    if request.method == 'POST':
        form = UserForms ( request.POST )
        if form.is_valid ():
            userName = form.cleaned_data['username']
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            eMail = form.cleaned_data['email']
            passWord = form.cleaned_data['password']
            confPassWord = form.cleaned_data['confirm_password']
            if passWord != confPassWord:
                return render ( request, 'design/reg_page.html', {'massage': 'Password did not mach'} )
            else:
                newUser = User ()
                newUser.username = userName
                newUser.first_name = firstName
                newUser.last_name = lastName
                newUser.email = eMail
                newUser.set_password ( passWord )
                newUser.save ()
                return redirect ()
        else:
            return HttpResponse ( 'Invalid Form' )

    return render ( request, 'design/reg_page.html' )
