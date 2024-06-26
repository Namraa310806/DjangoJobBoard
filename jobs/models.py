from django.db import models

# Create your models here.
class Job(models.Model):
    sno = models.AutoField(primary_key=True)
    Company = models.CharField(max_length=50)
    Job_title = models.CharField(max_length=100)
    Skills_required = models.TextField()
    Job_type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Company}-{self.Job_title}"   



class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    job = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.position}"


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name