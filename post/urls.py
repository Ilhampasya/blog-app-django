from .views import *
from .apps import PostConfig
from django.urls import path

app_name = PostConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('<id>/', read, name='read')
]