from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="India"
    return render(request,"index.html",{'obj':name})

def about(request):
    return render(request,'about.html')


def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res=x+y
    return render(request,"result.html",{'result':res})