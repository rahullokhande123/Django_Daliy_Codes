from django.shortcuts import render

# Create your views here.
def home(request):

    data1={
        'name':'Rahul Lokhande',
        'age':24,
        'quli':'BCA'
    }
    data2={
        'name':'Arun Silawat',
        'age':30,
        'quli':'B Sc.'
    }
    data3={
        'name':'Mohit',
        'age':26,
        'quli':'B.Tec'
    }
    return render(request,'home.html',{'key1':data1,'key2':data2,'key3':data3})
