from django.urls import path
from . import views # . means this

urlpatterns = [
    path('', views.index, name='index'), # '' as empty = home page
    path('post/<str:pk>', views.post, name='post')
]