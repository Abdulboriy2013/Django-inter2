from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_profile(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")
