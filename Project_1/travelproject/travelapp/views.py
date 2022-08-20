from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="India"
    return render(request,"index.html",{'obj':name})

def about(request):
    return render(request,'about.html')