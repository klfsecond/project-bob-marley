from django.urls import path
from . import views

urlpatterns = [
    path('agents', views.agents, name='agents'),
    path('agent_details', views.agent_details, name='agent_details'),
]