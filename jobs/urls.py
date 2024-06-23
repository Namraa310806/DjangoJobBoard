from django.urls import include, path

from jobs import views

urlpatterns = [
    path('',views.home),
    path('jobs/',views.jobs),
    path('job/apply/<str:com>/<str:tit>/<int:no>',views.userform),
    path('jobs/<str:slug>',views.detail),
    path('job/create/',views.companyform)

]
