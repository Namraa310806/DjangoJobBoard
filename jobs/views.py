from django.http import HttpResponse
from django.shortcuts import render


from jobs.models import Job,Application

# Create your views here.
def home(request):
    return render(request,"home.html")
def jobs(request):
    job=Job.objects.all()
    context = {'job':job}
    return render(request,"jobs.html",context)
def form(request):
    if request.method == "POST":
        full_name=request.POST['full_name']
        email=request.POST['email']
        phone=request.POST['phone']
        position=request.POST['position']
        resume=request.POST['resume']
        cover_letter=request.POST['cover_letter']
        linkedin=request.POST['linkedin']
        job=Job(full_name=full_name,email=email,phone=phone,position=position,resume=resume,cover_letter=cover_letter,linkein=linkedin)
    return render(request,"form.html")
