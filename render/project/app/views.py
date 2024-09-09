#redirect

# from django.shortcuts import render,redirect   -> for redirect


# Create your views here.
# def home(request):
#     # return render(request,'home.html')
#     return redirect('https://www.google.co.in/')


# ===================================================

from django.http import JsonResponse
def home(request):
    data={
        'name':'Rahul',
        'city':True,
        'age':24,
        'phd':None
    }
    return JsonResponse(data)
