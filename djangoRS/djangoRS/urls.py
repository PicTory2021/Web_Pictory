"""djangoRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import appRS.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appRS.views.index, name='index'),
    path('index/', appRS.views.get_user, name='user'),
    path('main/', appRS.views.main, name='main'),
    path('result/', appRS.views.result, name='result'),
    path('result/click', appRS.views.detailClick, name='result/click'),
    path('result/<int:id>/', appRS.views.result, name='result'),
    path('eval/',appRS.views.eval,name='eval'),
    path('nearLocation/', appRS.views.nearLocation, name='nearLocation'),
    path('getContext/', appRS.views.getContext, name='getContext'),
]
