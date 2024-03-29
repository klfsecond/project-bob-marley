from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('portal', views.PortalView.as_view(), name='portal'),
    path('your_listings', views.YourListingsView.as_view(), name='your_listings'),
    path('<int:application_id>', views.ApplicationView.as_view(), name='application'),

]
