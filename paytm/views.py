from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
import random
from paytm import Checksum
from django.contrib.auth.models import User

from paytm.models import PaytmHistory
# Create your views here.

# @login_required
def home(request):
    return HttpResponse("<html><a href='"+ settings.HOST_URL +"/paytm/payment'>PayNow</html>")


# def payment(request):
#     try:
#         print('4---------', request.user)
#         MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
#         MERCHANT_ID = settings.PAYTM_MERCHANT_ID
#         get_lang = "/" + get_language() if get_language() else ''
#         CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
#         # Generating unique temporary ids
#         order_id = Checksum.__id_generator__()

#         bill_amount = 50
#         if bill_amount:
#             # data_dict = {
#             #             'MID':"BUfEWY28036097078675",
#             #             'ORDER_ID':str(order_id),
#             #             'TXN_AMOUNT':str(bill_amount),
#             #             'CUST_ID':'harih@pickrr.com',
#             #             'INDUSTRY_TYPE_ID':'Retail',
#             #             'WEBSITE':settings.PAYTM_WEBSITE,
#             #             'CHANNEL_ID':'WEB',
#             #             'CALLBACK_URL':'http://localhost:8000/paytm/response',
#             #         }

#             data_dict = {

#                 'MID': MERCHANT_ID,
#                 'ORDER_ID': str(67),
#                 'TXN_AMOUNT': str(100),
#                 'CUST_ID': 'vipulshri4@gmail.com',
#                 'INDUSTRY_TYPE_ID': 'Retail',
#                 'WEBSITE': 'WEBSTAGING',
#                 'CHANNEL_ID': 'WEB',
#                 'CALLBACK_URL':'http://127.0.0.1:8000/paytm/response/',

#         }
            
#             param_dict = data_dict        
#             param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#             print(param_dict['CHECKSUMHASH'])
#             return render(request,"payment.html",{'paytmdict':param_dict})
#         return HttpResponse("Bill Amount Could not find. ?bill_amount=10")
#     except Exception as e:
#         print('error in paytm payment function', str(e))
#         return HttpResponse(str(e))


def payment(request):
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    CALLBACK_URL = settings.HOST_URL+ settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    bill_amount = 10
    if bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':str(order_id),
                    'TXN_AMOUNT': str(bill_amount),
                    'CUST_ID':'eieojiojoi@gmail.com',
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL': CALLBACK_URL,
                    }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,"payment.html",{'paytmdict':param_dict})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")

@csrf_exempt
def response(request):
    try:
        if request.method == "POST":
            MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
            data_dict = {}
            for key in request.POST:
                data_dict[key] = request.POST[key]
            verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
            if verify:
                 
                user_obj = User.objects.get(username = request.COOKIES.get('ucno'))
                PaytmHistory.objects.create(user = user_obj, **data_dict)
                return redirect('/profile/orders')
            else:
                return HttpResponse("checksum verify failed")
        return HttpResponse(status=200)

    except Exception as e:
        print('error in paytm respose', str(e))
        return HttpResponse(status=400)