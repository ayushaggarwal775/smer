from django.shortcuts import render , redirect
from django.http import HttpResponse
import requests
from user_profile import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import random
def send_otp(request):
    try:
        if(request.COOKIES.get('loggedIn')):
            responsetoredirect = redirect('/profile/')
            return responsetoredirect
        elif(request.method == 'POST'):
            no = request.POST['number']
            response = requests.get('https://2factor.in/API/V1/7e7c9082-0616-11ea-9fa5-0200cd936042/SMS/%s/AUTOGEN' % no)
            msg = response.json()
           
            return render(request, 'confirm_otp.html', {
                'Status': msg['Status'],
                'Details': msg['Details'],
                'cno' : no
            })
        
    except Exception as e:
        print('error in sending otp', str(e))
    return render(request,'login.html')

def verify_otp(request):
    try:
        if(request.method == 'POST'):
            otp = request.POST['otp']
            session_id = request.POST['Details']
            cno = request.POST['cno']
            response = requests.get('https://2factor.in/API/V1/7e7c9082-0616-11ea-9fa5-0200cd936042/SMS/VERIFY/%s/%s' % (session_id , otp))
            msg = response.json()
            print('verify otp ', msg)
            if(msg['Status'] == 'Success'):
                password = random.randint(100000000, 999999999)
                if User.objects.filter(username=cno).exists() is False:
                    user = User.objects.create_user(username = cno, password = 'abc')
                auth = authenticate(request, username = cno, password = 'abc')
                login(request, auth)
                user_profile = models.User.objects.get_or_create(contact_number = cno)
                # responsetosend = render(request, 'welcome.html',{
                #     'Status': msg['Status'],
                #     'Details': msg['Details']
                # })  
                responsetosend = redirect('/profile/')
                responsetosend.set_cookie(key='loggedIn', value=True , max_age=60*60*24)
                responsetosend.set_cookie(key='ucno', value=cno,max_age=60*60*24)
                print('2------------', request.user, auth)
                return responsetosend
            return render(request, 'confirm_otp.html', {
                'Status': msg['Status'],
                'Details': msg['Details']
            })
    except Exception as e:
        print('exception in verify otp', e)
        return render(request,'confirm_otp.html')
    

def forgot_view(request):
    return render(request,'forgot_pass.html')