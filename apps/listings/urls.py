from django.urls import path
from . import views
# listings
urlpatterns = [
    path('', views.IndexView.as_view(), name='listings'),
    path('<int:listing_id>', views.lisitng, name='listing'),
    path('search', views.search, name='search'),
    path('create_rental', views.CreateRentalListingView.as_view(), name='create_rental'),
]
