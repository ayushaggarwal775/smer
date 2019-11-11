from django.urls import path , include
#from django.conf.urls import include, url
from multiple_post import views

urlpatterns = [
    path('', views.get_multiple , name="get_multiple" ),
]