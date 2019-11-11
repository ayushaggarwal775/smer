from django.urls import path
#from django.conf.urls import include, url
from register import views

urlpatterns = [
    path('register', views.register_view,name='register'),
]
