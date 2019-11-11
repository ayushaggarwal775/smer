from django.shortcuts import render
from .models import Multiple

# Create your views here.
def get_multiple(request):
    if request.method == 'POST':
        print('in post')
        user = Multiple()
        #user.project = request.GET['projectname']
        
        user.From = request.GET['From']
        user.To = request.GET['To']
        user.typeofdel = request.GET['typeofdel']
        user.del_pin_no = request.GET['del_pin_no']
        user.weightrate = request.GET['weightrate']
        user.Describe_del = request.GET['Describe_del']
        user.pin_no = request.GET['typeofdel']
        user.Full_name = request.GET['del_pin_no']
        user.mobile_number = request.GET['weightrate']
        user.Flat_number_and_building_name = request.GET['Describe_del']
        user.Area = request.GET['Full_area_address']
        user.Land_mark = request.GET['Full_area_address']
        
        print(user.Area)
        user.save()
        context = {
            'message': 'Thanks for Submission'
        }
        print("done")
        # return render(request , 'dbo/projectdetail.html', context)
    
    else:

        # data = userprofile.objects.all()
        # print(data)

        context = {
            'message': 'Enter your project',
            #'data': 'data'
        }
        print('in else')
    
    return render(request,'multiple.html')
