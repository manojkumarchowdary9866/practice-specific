from django.urls import path
from app20.views import app20
app_name='app20'
urlpatterns=[
    path('app20/',app20,name='app20'),
]