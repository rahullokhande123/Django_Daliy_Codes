from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse 

# Create your views here.
def firstRender(request):
    return render(request,'home.html')

# def firstRender1(request):
#     return http("html contain")

# def firstRender2(request):
#     return JsonResponse(data)

# def firstRender3(request):
#     return redirect("url")