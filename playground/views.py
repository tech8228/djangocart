from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
import logging



logger = logging.getLogger(__name__) #playground.views




# Class Based View
class HelloView(APIView):
    
    
   # @method_decorator(cache_page(5*60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response= requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Classed based Cache'})


""" 
# Function Based View
@cache_page(5*60)
def say_hello(request):
    response= requests.get('https://httpbin.org/delay/2')
    data = response.json()
     
    return render(request, 'hello.html', {'name': data})
 """

# def say_hello(request):
#     notify_customers.delay('HelloDelayview')
#     return render(request, 'hello.html', {'name': 'Celery worker task check page'})




