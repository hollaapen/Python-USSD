from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to Wetiba subscription service \n"
            response += "1. Sport \n"
            response += "2. politics \n"
            response += "3. Local  \n"
            response += "4. International"


        elif text == "1":
            response = "CON Select Your Preferred Sport Plans \n"
            response += "1. Daily @ 15 \n"
            response += "2. Weekly @ 10 \n"
            response += "3. Monthly @ 5 "

        elif text == "1*1":
            response = "CON You will be charged KES 15 for your Daily Sports news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"


        elif text == "1*1*1":
            response = "END thank you for subscribing to our daily sport news plan \n"
        elif text == "1*1*2":
            response = "END thank you for your one-off daily sport news plan \n"

        elif text == "1*2":
            response = "CON You will be charged KES 10 for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"


        elif text == "1*2*1":
            response = "END thank you for subscribing to our weekly sport news plan \n"
        elif text == "1*2*2":
            response = "END thank you for your one-off weekly sport news plan \n"

        elif text == "1*3":
            response = "CON You will be charged KES 5 for our monthly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*3*1":
            response = "END thank you for subscribing to our monthly sport news plan \n"

        elif text == "1*3*2":
            response = "END thank you for your one-off monthly sport news plan \n"

        return HttpResponse(response)

# Create your views here.
