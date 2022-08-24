from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        conf_password = request.POST['password2']

        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.save()
            print("User Created")
        else:
            print("Password not Matching")

    return render(request, "register.html")
