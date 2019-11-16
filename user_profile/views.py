from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def get_user_profile(request):
    user = User.objects.get(username=request.user.username)
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

class orders(View):
    def get(self, request):
        user_obj = User.objects.get(username = request.user.username)
        orders = list(user_obj.rel_payment_paytm.all().values())
        print('orders ', orders)
        return render(request, 'orders.html', {"msg": "success", "orders": orders})