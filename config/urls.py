from django.contrib import admin
from django.urls import path, include
from maqola.views import about, index, detail
from maqola.views import like_post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('maqola/<int:id>/', detail, name='detail'),
    path('users/', include('users.urls')),
    path('like_post/<int:id>', like_post, name='like_post'),

]
    