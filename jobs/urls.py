from django.urls import include, path

from jobs import views

urlpatterns = [
    path('',views.home),
    path('jobs/',views.jobs),
    path('job/apply/<str:com>/<str:tit>/<int:no>',views.userform),
    path('jobs/<str:slug>',views.detail),
    path('job/create/',views.companyform),
    path('company/',views.company),
    path('job/list/<str:cmp>',views.list),
    path('update/<int:no>/<str:cmp>/<str:tit>/<str:skills>/<str:type>/',views.update),
    path('delete/<int:no>/',views.delete),
    path('applications/<int:no>/',views.app)

]
