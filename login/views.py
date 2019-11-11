from django.shortcuts import render , redirect
from django.http import HttpResponse
import requests
from user_profile.models import User

def send_otp(request):
    if(request.COOKIES.get('loggedIn')):
        responsetoredirect = redirect('/profile/')
        return responsetoredirect
    elif(request.method == 'POST'):
        no = request.POST['number']
        response = requests.get('https://2factor.in/API/V1/8b16b93c-ef4f-11e9-b828-0200cd936042/SMS/%s/AUTOGEN' % no)
        msg = response.json()
        return render(request, 'confirm_otp.html', {
            'Status': msg['Status'],
            'Details': msg['Details'],
            'cno' : no
        })
    return render(request,'login.html')

def verify_otp(request):
    if(request.method == 'POST'):
        otp = request.POST['otp']
        session_id = request.POST['Details']
        cno = request.POST['cno']
        response = requests.get('https://2factor.in/API/V1/8b16b93c-ef4f-11e9-b828-0200cd936042/SMS/VERIFY/%s/%s' % (session_id , otp))
        msg = response.json()
        if(msg['Status'] == 'Success'):
            user = User.objects.get_or_create(contact_number=cno)
            responsetosend = render(request, 'welcome.html',{
                'Status': msg['Status'],
                'Details': msg['Details']
            })  

            responsetosend.set_cookie(key='loggedIn', value=True , max_age=60*60*24)
            responsetosend.set_cookie(key='ucno', value=cno,max_age=60*60*24)
            return responsetosend
        return render(request, 'confirm_otp.html', {
            'Status': msg['Status'],
            'Details': msg['Details']
        })
    return render(request,'confirm_otp.html')


def forgot_view(request):
    return render(request,'forgot_pass.html')