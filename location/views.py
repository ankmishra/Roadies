# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from login.models import Profile
import requests
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

# Create your views here.

def home(request):
	if request.user.is_authenticated():
		sessions = Session.objects.filter(expire_date__gte=timezone.now())
		uid_list = []
		d = []
		# Build a list of user ids from that query
		for session in sessions:
			data = session.get_decoded()
			#obj = Profile.objects.get(user_id=data.get('_auth_user_id', None))
			#uid_list.append(data.get('_auth_user_id', None))
			user = Profile.objects.filter(user_id=data.get('_auth_user_id', None)).values('lat','lon')
			uid_list.append(Profile.objects.filter(user_id=data.get('_auth_user_id', None)).values('lat','lon'))
			d.append(list(user))
		#j = json.loads(r.text)
			#lat = user.lat
		#lon = j['Longitude']
		#location= j['city']
		#name = request.user.username
		#user = get_object_or_404(User, pk='1')
		
		#obj = Info.objects.get(user_=sub)
		#Profile.objects.filter(user_id=user_id).update(name=name,user_id=user_id,lat=lat,lon=lon,location=location)
		#loc.save(),{'lat':lat,'lon':lon}
		#d = JsonResponse({'results': list(uid_list[0])})

		return render(request, 'location.html',{'d':d})
	else:
		return HttpResponseRedirect("/login")


	#response = requests.get('https://maps.googleapis.com/maps/api/js?key=AIzaSyCoEaVOtziAEr1bpEeVF07HQvL9PhZsLPA&callback=initMap')
	#print response.status_code
	#
	
	#d =  json.dumps(list(uid_list[0]))
	#return HttpResponse(d)
def update(request):
    	lat = request.GET['lat']
    	lon = request.GET['lng']
    	name = request.user.username
    	#user = get_object_or_404(User, pk='1')
    	user_id = User.objects.get(username=request.user).pk
    	#obj = Info.objects.get(user_=sub)
    	Profile.objects.filter(user_id=user_id).update(name=name,user_id=user_id,lat=lat,lon=lon)
    	#loc.save()
    	return HttpResponse('sucessfully updated')
#def latlon(request):



    

