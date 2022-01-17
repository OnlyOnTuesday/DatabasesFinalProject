"""GitStalker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

import GitStalker.views as views

# urlpatters requires certain urls to be defined twice, for when they do and when
# they don't have arguments.  I think this is worth it for slightly cleaner code

urlpatterns = [
    path('', views.home_page),
    path('index/', views.home_page),
    path('getWmName/<str:wm_name>/', views.getWmView, name='getWmName'),
    path('getWmName/', views.getWmView, name='getWmName'),
    path('getUserView/<str:usr_name>/',views.getUserView, name='getUserView'),
    path('getUserView/',views.getUserView, name='getUserView'),
    path('admin/', admin.site.urls),
]
