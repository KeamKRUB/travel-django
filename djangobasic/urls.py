"""djangobasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs import views


urlpatterns = [
#travel
    path('', views.home),
    path('admin/', admin.site.urls),
    path('travel', views.travel),
    path('travel/park', views.parka),
    path('travel/nature', views.naturea),
    path('travel/park/waterfall', views.waterfallap),
    path('travel/park/forest', views.forestap),
    path('travel/park/mountain', views.mountainap),
#Views
    path('views', views.views),
    path('views/park', views.parkv),
    path('views/nature', views.naturev),
    path('views/park/waterfall', views.waterfallvp),
    path('views/park/forest', views.forestvp),
    path('views/park/mountain', views.mountainvp),
    path('travel/park/sea', views.seavp),
    path('travel/nature/waterfall', views.waterfallan),
    path('travel/nature/forest', views.forestan),
    path('travel/nature/mountain', views.mountainan),
    path('travel/nature/sea', views.seaan),
    path('home', views.home),
]
