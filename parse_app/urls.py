from django.urls import path
from .views import *

urlpatterns = [
    path('', finish_parser_views,name='test_link')
]