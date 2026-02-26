from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from maqola.models import Maqola, Comment
from .models import Profile

#* Login profile
def login_profile(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  
        else:
            print("Login failed: Invalid username or password")
            return render(request, "login.html")
    else:

        return render(request, "login.html")
    


#? Sign up
def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        user = Profile.objects.create_user(email=email, password=password, first_name=name, last_name=last_name)
        login(request, user)
        return redirect('profile')
    else:
        return render(request, "sign_up.html")
    


#* Logout profile
def logout_profile(request):
    logout(request)
    return redirect('login_profile')



#! Profile
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_profile')
    return render(request, "profile.html") 
