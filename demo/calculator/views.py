from django.shortcuts import render
from django.shortcuts import HttpResponse

def calc(request):
    return render(request,'Home.html')

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    result=val1+val2
    return render(request,'calculate.html',{'ans':result})