from django.shortcuts import render

# Create your views here.
def secret_index( request ):
    return render( request, "secret/secret_index.html" )