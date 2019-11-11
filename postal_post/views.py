from django.shortcuts import render
from .models import Postal
from django.http import HttpResponse

# Create your views here.
def get_postal(request):
    if request.method == 'POST':
        postal_order = Postal()
        postal_order.From = request.POST['From']
        postal_order.To = request.POST['To']
        postal_order.del_pin_no = request.POST['del_pin_no']
        postal_order.Describe_del = request.POST['Describe_del']
        postal_order.Full_area_address = request.POST['Full_area_address']
        postal_order.save()
        return HttpResponse("Created new order")
    
    return render(request,'postal.html')

#def (request):