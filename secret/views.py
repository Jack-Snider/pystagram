from django.shortcuts import render
from .models import Sender

# Create your views here.

def sender( request ):

    return render( request, "secret/sender.html" )

def receiver( request ):

    if request.method == "POST":

        message = request.POST[ 'message' ]

        context = {
            'message' : message
        }

        # Sender 모델에 저장
        sender = Sender()
        sender.message = message
        sender.save()

    return render( request, "secret/receiver.html", context )




