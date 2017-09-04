"""roadies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from login import views as core_views
from location import views as loc_views
from chat import views as chat_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
     url(r'^sign$', core_views.sign, name='sign'),
    #url(r'^logusers/$', core_views.logusers, name='logusers'),
    url(r'^location/$', loc_views.location, name='location'),
    url(r'^latlon/$', loc_views.update, name='update'),
     url(r'^message/$', chat_views.message, name='message'),
     url(r'^chat/$', chat_views.chat, name='chat'),
]
