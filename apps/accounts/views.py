from django.shortcuts import render, redirect
from django.contrib import messages, auth
from apps.accounts.models import ClientModel as User
from apps.contacts.models import Contacts

# Create your views here.
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match 
        if password==password2:
            #check email
            if User.objects.filter(email=email).exists():
                messages.error(request,'That email is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(password=password, email=email)
                    # Login after register
                    # auth.login(request,user)
                    # messages.success(request,'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts= Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
