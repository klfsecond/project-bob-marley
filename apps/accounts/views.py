from django.shortcuts import render, redirect
from django.views import View
# from django.contrib.auth import authenticate, login
from apps.authentication.forms import LoginForm, SignUpForm
from django.contrib import messages, auth
from apps.accounts.models import ClientModel as User
from apps.contacts.models import Contacts
from apps.listings.models import ListingModel


# Create your views here.
# def register(request):
#     if request.method =='POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         # check if passwords match 
#         if password==password2:
#             #check email
#             if User.objects.filter(email=email).exists():
#                 messages.error(request,'That email is taken')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request,'That email is being used')
#                     return redirect('register')
#                 else:
#                     user = User.objects.create_user(password=password, email=email)
#                     # Login after register
#                     # auth.login(request,user)
#                     # messages.success(request,'You are now logged in')
#                     # return redirect('index')
#                     user.save()
#                     messages.success(request,'You are now registered and can log in')
#                     return redirect('login')

#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')

#     else:
#         return render(request,'accounts/register.html')

class RegisterView(View):
    template_name = "accounts/register.html"

    def get(self,request):
        form = SignUpForm()
        return render(request, self.template_name,context={"form":form})
    
    def post(self,request):
        form = SignUpForm(request.POST)
        password    = request.POST['password']
        password2   = request.POST['password2']        
        if form.is_valid() and str(password) == str(password2) and not User.objects.filter(email=request.POST['email']).exists() :
            user = User.objects.create_user(password=password, email=request.POST['email'])
            form.save()
            return redirect('login')
        elif form.errors:
            messages.add_message(request, messages.ERROR , f"Oops! {form.error_messages}")
            return redirect('register')


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self,request):
        form = LoginForm(request.GET)
        return render(request, self.template_name, context={"form":form})
    
    def post(self,request):
        form     = LoginForm(request.POST or None)
        print(form.data)
        username = form.data["username"]
        password = form.data["password"]
        user     = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.add_message(request, messages.SUCCESS , f"Welcome back {user}!")
            auth.login(request, user)
            return redirect("/")
        return redirect('home')

# This needs a DB Change to work, add owner to property listing model.
class PortalView(View):
    template_name = ''

    def get(self,request):
        listings = ListingModel.objects.filter()
        active_listings = listings.filter(is_published=True)
        inactive_listings = listings.filter(is_published=True)
        context = {
            active_listings : active_listings,
            inactive_listings : inactive_listings
        }
        return render(request,self.template_name,context)
# This needs a DB Change to work, add owner to property listing model.

# This needs work
class LogOutView(View):

    def get(request,self):
        print(request)
        print(request.request.body )
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
# This needs work


def dashboard(request):
    user_contacts= Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
