from django.http import HttpResponse
from django.shortcuts import render


from jobs.models import Job,Application

# Create your views here.
def home(request):
    three_jobs = Job.objects.all()[:3]
    return render(request,"home.html",{'job':three_jobs})

def jobs(request):
    job=Job.objects.all()
    context = {'job':job}
    return render(request,"jobs.html",context)

def userform(request,com,tit,no):
    context={'success':False,'Company':com,'pos':tit}
    if request.method == "POST":
        full_name=request.POST['full_name']
        email=request.POST['email']
        phone=request.POST['phone']
        resume=request.POST['resume']
        cover_letter=request.POST['cover_letter']
        linkedin=request.POST['linkedin']
        applicant=Application(full_name=full_name,email=email,phone=phone,position=tit,resume=resume,cover_letter=cover_letter,linkedin=linkedin,job=no)
        applicant.save()
        context={'success':True,'Company':com,'pos':tit}
    return render(request,"userform.html",context)

def detail(request,slug):
    job=Job.objects.filter(Job_title=slug)
    return render(request,'detail.html',{'job':job, 'slug':slug})

def companyform(request):
    context={'success':False}
    if request.method=="POST":
        company=request.POST['company']
        job_title=request.POST['job_title']
        skills_required=request.POST['skills_required']
        job_type=request.POST['job_type']
        j1= Job(Company=company,Job_title=job_title,Skills_required=skills_required,Job_type=job_type)
        j1.save()
        context={'success':True}
    return render(request,"companyform.html",context)



