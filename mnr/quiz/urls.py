from django.urls import path, include
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.Index, name='index'),
]