from django.urls import path
from . import views

urlpatterns = [
    path('pages', views.index, name='index'),
    path('pages', views.about, name='about'),
]