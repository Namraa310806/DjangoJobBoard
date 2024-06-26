from django.contrib import admin
from jobs.models import Company, Job,Application, User
# Register your models here.
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(User)
admin.site.register(Company)