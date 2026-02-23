from django.contrib import admin
from django.urls import path, include
from maqola.views import about, index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('maqola/<int:id>/', detail, name='detail'),
    path('users/', include('users.urls'))
]
