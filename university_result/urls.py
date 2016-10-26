"""university_result URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from results import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', views.welcome, name='home'),
    url(r'^hi/', views.hi, name='home'),
    #url(r'^articles/([0-9]{4})/$', views.special_case_2003),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    
     url(r'^articles/(?P<year>[0-9]{4})/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})/$', views.special_case_2016),
    url(r'^person_registrations/$', views.person_register),
     url(r'^$', views.index, name='index'),
]
