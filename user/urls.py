from  django.urls import path
from  . import views

urlpatterns=[
    path('',views.index),
    path('view',views.V),
    path("home",views.home),
    path('logout',views.logout),
    path('login',views.login),
    path('registration',views.reg),
    path('prd',views.prd)
]
