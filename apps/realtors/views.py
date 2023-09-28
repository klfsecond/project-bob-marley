from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from apps.realtors.models import Realtor 

# Create your views here.

def agents(request):
    realtors=Realtor.objects.order_by('-hire_date')

    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

    context= {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(request, 'pages/agents.html', context)

def agent_details(request):

    return render(request, 'pages/agent_details.html', {})