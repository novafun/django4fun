from django.urls import path
from . import views

urlpatterns = [
    # The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
    path('', views.index, name='index'),  # the index matches the function name in views.py
]
