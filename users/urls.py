from django.urls import path, include
from .views import login_profile
from .models import Profile

urlpatterns = [
    path('login/', login_profile, name='login_profile'),
    # path('profile/', profile, name='profile'),
]
