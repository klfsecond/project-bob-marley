from django.shortcuts import get_object_or_404, render, redirect
from apps.listings.models import (ListingModel)
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from apps.listings.choices import price_choices, bedroom_choices, state_choices
from .forms import CreateRentalListing

# Create your views here.

def create_rental_listing(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = CreateRentalListing(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves the instance to the database
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            return redirect('/listings')  # Redirect to a success page or the same page
        else:
            msg = 'Form is not valid'
    else:
        form = CreateRentalListing() 
    
    return render(request, 'listings/create_rental_listing.html', {"form": form, "msg": msg, "success": success})


def index(request):
    listings = ListingModel.objects.order_by('-list_data').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def lisitng(request, listing_id):
    listing=get_object_or_404(ListingModel, pk=listing_id)

    context={
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list=ListingModel.objects.order_by('-list_data')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
        
   #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact = city)

     #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list=queryset_list.filter(city__iexact = state)
    
    
     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
                
    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }

    return render(request, 'listings/search.html', context)
