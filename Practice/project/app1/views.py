from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
# def home(request):
#     # return http("<h1>I am Rahul </h1>")
#     return HttpResponse('''<h1 style="background-color:red"> Dear Django , This is my first page</h1>''')

def firstRender(request):
    return render(request,'home.html')

def myredirect(request):
    return redirect("https://github.com/")

def myJsonResponse(request):
    return JsonResponse([{name:"Rahul"}])

