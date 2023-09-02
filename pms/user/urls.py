from django.contrib import admin
from . import views
from django.urls import path,include
from .views import *
# from django.contrib.auth.views import LogoutView
urlpatterns = [

 path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
 path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
 path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
 path('teamleaderregister/',TeamLeaderRegisterView.as_view(),name='teamleaderregister'),
 path('testerregister/',TesterRegisterView.as_view(),name='testerregister'),
 path('login/',UserLoginView.as_view(),name ='login'),
 path('logout/',views.logoutUser,name='logout'),
 path('sendmail/',views.sendMail,name='sendmail'),
 path('admin/dashboard/',AdminDashboardView.as_view(),name='admin_dashboard'),
 path('manager/dashboard/',ManagerDashBoardView.as_view(),name='manager_dashboard'),
 path('developer/dashboard/',DeveloperDashBoardView.as_view(),name='developer_dashboard'),
    
]
