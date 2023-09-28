from django.urls import path
from . import views
# listings
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.lisitng, name='listing'),
    path('search', views.search, name='search'),
    path('create_rental', views.create_rental_listing, name='create_rental'),
]
