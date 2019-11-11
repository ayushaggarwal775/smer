from django.urls import path , include
#from django.conf.urls import include, url
from postal_post import views

urlpatterns = [
    path('', views.get_postal , name="get_postal" ),
    
]