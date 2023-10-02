from django.shortcuts import render, redirect
from django.views import View
# from django.contrib.auth import authenticate, login
from apps.authentication.forms import LoginForm, SignUpForm
from django.contrib import messages, auth
from apps.accounts.models import ClientModel as User
from apps.contacts.models import Contacts
from apps.listings.models import ListingModel, PropertyApplicationModel,PropertyViewingModel



class RegisterView(View):
    template_name = "accounts/register.html"

    def get(self,request):
        form = SignUpForm()
        return render(request, self.template_name,context={"form":form})
    
    def post(self,request):
        form      = SignUpForm(request.POST)
        password  = request.POST['password']
        password2 = request.POST['password2']
        if form.is_valid() and str(password) == str(password2) and not User.objects.filter(email=request.POST['email']).exists() :
            user = User.objects.create_user(password=password, email=request.POST['email'])
            user.set_password(password)
            messages.add_message(request, messages.SUCCESS , f"! {form}")
            return redirect('login')
        
        elif form.errors:
            messages.add_message(request, messages.ERROR , f"Oops! {form}")
            return redirect('register')


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self,request):
        form = LoginForm(request.GET)
        return render(request, self.template_name, context={"form":form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data["username"]
            password = form.data["password"]
            user     = auth.authenticate(username=username, password=password)
            if user is not None:
                messages.add_message(request, messages.SUCCESS , f"Welcome back {user}!")
                auth.login(request, user)
                return redirect("/")
            # No User Found
            messages.add_message(request, messages.ERROR , f"We could not find an account matching your email. Please check and try again!")
            return redirect('login')
        # Form Errors
        messages.add_message(request, messages.ERROR , f"Oop! {form.errors}")
        return redirect('login')

# This needs work
class LogOutView(View):
    def get(request,self):
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
# This needs work

# This needs a DB Change to work, add owner to property listing model.
class PortalView(View):
    template_name = "accounts/portal.html"

    def get(self,request):
        listings                    = ListingModel.objects.filter(landlord=request.user)
        # ACTIVE LISTINGS
        active_listings             = listings.filter(is_published=True)
        active_listings_count       = active_listings.count()
        # INACTIVE LISTINGS
        inactive_listings           = listings.filter(is_published=True)
        inactive_listings_count     = inactive_listings.count()
        # VIEWINGS - Client 
        client_viewing_appointments        = PropertyViewingModel.objects.filter(application__client=request.user)
        client_viewing_appointments_count  = client_viewing_appointments.count()
        # VIEWINGS - Landlord
        landloard_viewing_appointments        = PropertyViewingModel.objects.filter(application__property__landlord=request.user)
        landloard_viewing_appointments_count  = landloard_viewing_appointments.count()
        # Messages 
        message_count = 0

        context = {
            "active_listings" : active_listings,
            "active_listings_count":active_listings_count,
            "inactive_listings" : inactive_listings,
            "inactive_listings_count":inactive_listings_count,
            'client_viewing_appointments':client_viewing_appointments,
            'client_viewing_appointments_count':client_viewing_appointments_count,
            'landloard_viewing_appointments':landloard_viewing_appointments,
            'landloard_viewing_appointments_count':landloard_viewing_appointments_count,
            'upcoming_viewings_total':landloard_viewing_appointments_count + client_viewing_appointments_count,
            'message_count':message_count
        }
        return render(request,self.template_name,context)
# This needs a DB Change to work, add owner to property listing model.

# 
class YourListingsView(View):
    template_name = "accounts/your_listings.html"

    def get(self,request):
        listings                    = ListingModel.objects.filter(landlord=request.user)
        # ACTIVE LISTINGS
        active_listings             = listings.filter(is_published=True)
        active_listings_count       = active_listings.count()
        context = {
            'active_listings':active_listings,
            'active_listings_count':active_listings_count
        }
        return render(request,self.template_name,context)




def dashboard(request):
    user_contacts= Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
