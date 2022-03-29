"""project15 URL Configuration

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
from django.urls import path,include
from app19.views import manoj1,manoj2
import app20

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manoj1/',manoj1,name='manoj1'),
    path('manoj2/',manoj2,name='manoj2'),
    path('app20/',include('app20.urls'),)

]
