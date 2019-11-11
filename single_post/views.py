from django.shortcuts import render
from .models import Single_Order
from django.http import HttpResponse
import requests
import json

# Create your views here.
def get_single(request):
    if(request.method == 'POST'):
        From = request.POST['From']
        To = request.POST['To']
        For = request.POST['For']
        Pin_No = request.POST['Pin No']
        Full_Name = request.POST['Full Name']
        Mobile_No = request.POST['Mobile No']
        Flat_No = request.POST['Flat-No']
        Area = request.POST['Area']
        Land_Mark = request.POST['Land Mark']
        City = request.POST['City']
        State = request.POST['State']
        new_single_order = Single_Order()
        new_single_order.From = From
        new_single_order.To = To
        new_single_order.pin_no = Pin_No
        new_single_order.Full_name = Full_Name
        new_single_order.mobile_number = Mobile_No
        new_single_order.Flat_number_and_building_name = Flat_No
        new_single_order.Area = Area
        new_single_order.Land_mark = Land_Mark
        new_single_order.City = City
        new_single_order.save()
        #return HttpResponse("Created new order:"+str(new_single_order))


        
        # Enter your source and destination city
        # originPoint = input("Please enter your origin city: ")
        # destinationPoint= input("Please enter your destination city: ")
        #Place your google map API_KEY to a variable
        # apiKey = 'YOUR_API_KEY'
        # #Store google maps api url in a variable
        # url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        # # call get method of request module and store respose object
        # r = requests.get(url + 'origins = ' + From + '&destinations = ' + To + '&key = ' + apiKey)
        # #Get json format result from the above response object
        # res = r.json()
        # #print the value of res
        # print(res)



        # context = {
        #             'From': From,
        #             'To': To,
        #             'For': For,
        #             'Full_Name': Full_Name,
        #             'Mobile_No': Mobile_No,
        #             'Flat_No': Flat_No,
        #             'Area': Area,
        #             'Land_Mark': Land_Mark,
        #             'City': City,               
        #         }


    return render(request,'single.html')


