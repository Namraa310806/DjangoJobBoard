from django.urls import include, path

from jobs import views

urlpatterns = [
    path('',views.home),
    path('jobs/',views.jobs),
    path('form/<str:com>/<str:tit>/<int:no>',views.form),
    path('jobs/<str:slug>',views.detail)

]
