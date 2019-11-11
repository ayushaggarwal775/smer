from django.urls import path , include
#from django.conf.urls import include, url
from user_profile import views

urlpatterns = [
    path('', views.get_user_profile , name="get_user_profile" ),
]