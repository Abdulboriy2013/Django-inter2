from django.urls import path, include
from .views import index, detail, comment

urlpatterns= [
    path('comment', comment, name='comment'),
    path('detail/<int:id>', detail, name='detail'),
    path('', index, name='index')
]