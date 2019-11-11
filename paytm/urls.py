#from django.conf.urls import include, url
from django.urls import path
from paytm import views

urlpatterns = [
    path('', views.home, name="home"),
    path('payment', views.payment, name="payment"),
    path('response', views.response, name="response"),
    #path('', views.get_single , name="get_single"),
]
