from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the polls directory, create a file called urls.py.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

