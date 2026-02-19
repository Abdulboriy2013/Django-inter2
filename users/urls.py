from django.urls import path, include

from maqola.views import detail
from .views import login_profile, logout_profile, profile, sign_up
from maqola.views import comment

urlpatterns = [
    path('login/', login_profile, name='login_profile'),
    path('logout/', logout_profile, name='logout_profile'),
    path('profile/', profile, name='profile'),
    path('sign_up/', sign_up, name='sign_up'),
    path('comment/', comment, name='comment'),
]
