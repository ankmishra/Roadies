# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from chat.models import Chat
import datetime


# Create your views here.
def message(request):
 	if request.method == 'POST':
 		sender_name = request.user.username
 		reciever = request.POST['user']
 		message = request.POST['meeasge']
 		now = datetime.datetime.now()
 		sender = User.objects.get(username=request.user.username)
 		chat = Chat.objects.create(sender=sender,reciever=reciever,message=message,sender_name=sender_name,time =now)
 		#user_id = User.objects.get(username=request.user).pk
 		#obj = Info.objects.get(user_=sub)
 		#Profile.objects.filter(user_id=user_id).update(name=name,number=number,location=location,typer=typer)
 		return redirect('/location/')
 	else:
 		form = SignUpForm()
 	return render(request, 'location.html', {'form': form})

def chat(request):
    reciver = request.user.username
    objreciever = Chat.objects.filter(reciever=reciver).values('sender_name','reciever','message')
    objsender = Chat.objects.filter(sender_name=reciver).values('sender_name','reciever','message')
    d =[]
    e=[]
    e.append(list(objsender))
    d.append(list(objreciever))
	#sender = User.objects.get(username=request.user.username)
	#chat = Chat.objects.create(sender=sender,reciever=reciever,message=message)
	#user_id = User.objects.get(username=request.user).pk
	#obj = Info.objects.get(user_=sub)
	#Profile.objects.filter(user_id=user_id).update(name=name,number=number,location=location,typer=typer)
    return render(request, 'chat.html',{'obj1':list(objreciever),'obj2':list(objsender)})
	#return HttpResponse(obj)
	#return redirect('/location/')
