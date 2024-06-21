# myapp/urls.py
from django.urls import path
from . import views  # Correct import statement


urlpatterns = [
    path('', views.index, name='index'),
]
