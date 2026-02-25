from django.urls import path, include
from .views import index, detail, comment, like_post

urlpatterns= [
    path('', index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
    path('comment', comment, name='comment'),
    path('like_post/<int:id>', like_post, name='like_post'),
]