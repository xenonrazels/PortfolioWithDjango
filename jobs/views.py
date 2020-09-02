from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.
from .models import Job

def home(request):
    content = {
        'jobs':Job.objects
    }
    return render(request, 'jobs/home.html', content)

def detail(request,job_id):
    content = {
        "details":get_object_or_404(Job,pk=job_id)
    }
    return render(request,'jobs/detail.html',content)