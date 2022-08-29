from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return HttpResponse("Hello, I am Homepage")


def about(request):
    return render(request,'about.html')


def home(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def details(request):
    return render(request,'details.html')


def thanks(request):
    return render(request,'thanks.html')

def calc(request):
    return render(request,'calculator.html')

def result(request):
    x=int(request.GET['num1'])
    y=request.GET['oper']
    z=int(request.GET['num2'])
    if y=='+':
        res=x+z
    elif y=='-':
        res=x-z
    elif y=='*':
        res=x*z
    elif y=='/':
        res=x/z
    else:
        res="Invalid Operator"
    return render(request,'result.html',{'result':res})