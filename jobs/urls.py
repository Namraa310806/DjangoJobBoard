from django.urls import include, path

from jobs import views

urlpatterns = [
    path('',views.userLogin),
    path('companyLogin/',views.companyLogin),
    path("userReg/",views.userReg),
    path("companyReg/",views.companyReg),
    path('userHome/',views.userHome),
    path('forgot-password/user/',views.forgotPasswordUser),
    path('forgot-password/company/',views.forgotPasswordCompany),
    path('companyHome/<str:cmp>',views.companyHome),
    path('jobs/',views.jobs),
    path('job/apply/<str:com>/<str:tit>/<int:no>',views.userform),
    path('jobs/<str:slug>',views.detail),
    path('job/create/<str:cmp>',views.createJob),
    path('job/list/<str:cmp>',views.list),
    path('update/<int:no>/<str:cmp>/<str:tit>/<str:skills>/<str:type>/',views.update),
    path('delete/<int:no>/<str:cmp>',views.delete),
    path('applications/<int:no>/',views.app)

]
