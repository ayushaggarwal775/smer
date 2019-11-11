from django.shortcuts import render
from user_profile.models import User
from django.http import HttpResponse

# Create your views here.
def get_user_profile(request):
    cno = request.COOKIES.get('ucno')
    user = User.objects.get(contact_number=cno)
    if(request.method == 'POST'):
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.country = request.POST['country']
        user.postal_code = request.POST['postal_code']
        user.save()
        return render(request,'profile.html',{
            'user':user,
            'status':'success',
            'msg':'Profile Updated '+request.POST['username']
        })
    return render(request,'profile.html',{
        'user':user,
        'status':'warning',
        'msg':'Update your Profile Information'
    })