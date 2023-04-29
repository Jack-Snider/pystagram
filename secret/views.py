from django.shortcuts import render

# Create your views here.
def secret_index( request ):
    return render( request, "secret/secret_index.html" )

def secret_intro( request ):

    if request.method == "POST":

        text = request.POST[ 'intro' ] # template에서 여기로 제출할때 input태그의 name 속성

        context = {
            "text" : text
        }

        return render( request, "secret/secret_intro.html", context )
