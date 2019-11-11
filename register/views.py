from django.shortcuts import render
from django.http import HttpResponse
from register.models import User

# Create your views here.
def register_view(request):
    if(request.method == 'POST'):
        name = request.POST['first_name']+request.POST['last_name']
        email = request.POST['email']
        contact_no = request.POST['contact_number']
        password = request.POST['password']
        user = User(name=name,email=email,contact_number=contact_no,password=password)
        user.save()
        return render(request,'login.html',{'message':'Registered Successfully'})
    return render(request,'register.html')