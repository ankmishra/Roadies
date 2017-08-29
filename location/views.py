# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
	#r = requests.get(send_url)
	#j = json.loads(r.text)
	#lat = j['latitude']
	#lon = j['longitude']
	return render(request, 'location.html')
	#response = requests.get('https://maps.googleapis.com/maps/api/js?key=AIzaSyCoEaVOtziAEr1bpEeVF07HQvL9PhZsLPA&callback=initMap')
	#print response.status_code
	#
	
	#return HttpResponse(lat)

    

