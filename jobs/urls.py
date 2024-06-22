from django.urls import include, path

import jobs

urlpatterns = [
    path('/',views.home),
    path('jobs/',views.jobs),
    path('form/',views.form)

]
