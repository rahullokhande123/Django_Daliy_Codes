from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('''<h1 style="background-color:red"> Dear Django , This is my first page</h1>'''+)
