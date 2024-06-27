from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import check_password


from jobs.models import Company, Job,Application, User

# Create your views here.
def userHome(request):
    three_jobs = Job.objects.all()[:3]
    return render(request,"userHome.html",{'job':three_jobs})

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

def createJob(request,cmp):
    if request.method == 'POST':
        job_title = request.POST['job_title']
        skills_required = request.POST['skills_required']
        job_type = request.POST['job_type']
        
        # Create a new job
        new_job = Job(Company=cmp, Job_title=job_title, Skills_required=skills_required, Job_type=job_type)
        new_job.save()
        
        # Redirect to the job listing page
        return redirect(f'/job/list/{cmp}')
    
    return render(request, 'jobCreate.html', {'cmp': cmp})



def list(request,cmp):
    jobs=Job.objects.filter(Company=cmp)
    return render(request,"jobsCompany.html",{'cmp':cmp,'job':jobs})

def update(request,no,cmp,tit,skills,type):
    success = False
    if request.method=="POST":
        job_instance = Job.objects.get(sno=no)
        job_instance.Company=request.POST['company']
        job_instance.Job_title=request.POST['job_title']
        job_instance.Skills_required=request.POST['skills_required']
        job_instance.Job_type=request.POST['job_type']
        job_instance.save();
        success=True
    content={'no':no,'cmp':cmp,'tit':tit,'skills':skills,'type':type,'success':success}
    return render (request,"update.html",content)

def delete(request,no,cmp):
    job = get_object_or_404(Job, sno=no)
    job.delete()
    return redirect('/job/list/'+cmp)

def app(request,no):
    apps=Application.objects.filter(job=no)
    return render(request,"application.html",{'apps':apps})

def userLogin(request):
    error = None

    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        try:
            user = User.objects.get(name=name)
            if password == user.password: 
                return redirect('/userHome')
            else:
                error = "Incorrect password."
        except User.DoesNotExist:
            error = "User not registered. Please create an account."

    return render(request, 'userLogin.html', {'error': error})

def companyLogin(request):
    error = None

    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        try:
            company = Company.objects.get(name=name)
            if password == company.password:
                return redirect('/companyHome/'+ company.name)
            else:
                error = "Incorrect password."
        except Company.DoesNotExist:
            
            error = "Company not registered. Please create an account."

    return render(request, 'companylogin.html', {'error': error})

def userReg(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not password:
            error="Please fill in all fields."
            return render(request, 'userRegister.html',{'error':error})

        if User.objects.filter(email=email).exists():
            error="User with this email already exists."
            return render(request, 'userRegister.html',{'error':error})

        new_user = User.objects.create(name=name, email=email, password=password)
        new_user.save()

        return redirect('/') 

    return render (request,"userRegister.html",{'error':error})

def companyReg(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not password:
            error="Please fill in all fields."
            return render(request, 'companyRegister.html',{'error':error})

        if Company.objects.filter(email=email).exists():
            error="Company with this email already exists."
            return render(request, 'companyRegister.html',{'error':error})

        new_company = Company.objects.create(name=name, email=email, password=password)
        new_company.save()
        return redirect('/companyLogin')
    return render (request,"companyRegister.html",{'error':error})

def companyHome(request,cmp):
    return render(request,"companyHome.html",{'cmp':cmp})