from django.urls import include, path

from jobs import views

urlpatterns = [
    path('',views.home),
    path('jobs/',views.jobs),
    path('form/',views.form)

]
