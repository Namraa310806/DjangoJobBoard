from django.http import HttpResponse
from django.shortcuts import render

from jobs.models import Job,Applicant

# Create your views here.
def home(request):
    return render(request,"home.html")
def jobs(request):
    job=Job.objects.all()
    context = {'job':job}
    return render(request,"jobs.html",context)
def form(request):
    return render(request,"form.html")
