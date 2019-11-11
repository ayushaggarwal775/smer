from django.urls import path
#from django.conf.urls import include, url
from login import views

urlpatterns = [
    path('', views.send_otp,name='send_otp'),
    path('login', views.send_otp,name='send_otp'),
    path('verify_otp', views.verify_otp,name='verify_otp'),
    path('forgot', views.forgot_view,name='forgot_pass'),
]
