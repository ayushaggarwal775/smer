from django.urls import path , include
from single_post import views
#from django.conf.urls import include, url

urlpatterns = [
    path('', views.get_single , name="get_single"),
     
]