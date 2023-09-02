from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import *
from django.views.generic import ListView,TemplateView
from project.models import Project
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import *
from project.views import *

# Create your views here.

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminCreationForm
    template_name = 'user/admin_register.html'
    success_url = "/user/login/"
    
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        user=form.save()
        recipient_list = [email]
        subject = "welcome to django"
        message = "Say hello to Django!! You are Admin now"
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
        #print(email)
        login(self.request,user)
        return redirect('/user/admin/dashboard/')

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerCreationForm
    template_name = 'user/manager_register.html'
    success_url = "/user/login/"

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = "Welcome to django"
        message = "Say hello to Django !! You are manager Now."
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject,message,email_from,recipient_list)
        login(self.request,user)
        return redirect('/user/manager/dashboard/')

class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperCreationForm
    template_name = 'user/developer_register.html'
    success_url = "/user/login/"
 
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = "Welcome to Django"
        message = "Say hello to Django !! You Are developer Now."        
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject,message,email_from,recipient_list)
        login(self.request,user)
        return redirect('/user/developer/dashboard/')


class TeamLeaderRegisterView(CreateView):
    model = User
    form_class = TeamLeaderCreationForm
    template_name = 'user/teamleader_register.html'
    success_url = '/user/login/'

    def get_context_data(self, **kwargs) :
        kwargs['user_type'] = 'team_leader'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class TesterRegisterView(CreateView):
    model = User
    form_class = TesterCreationForm
    template_name = 'user/tester_register.html'
    success_url = '/user/login/'

    def get_context_data(self, **kwargs) :
        kwargs['user_type'] = 'tester'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = '/'
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager/dashboard/'
            elif self.request.user.is_admin:
                return '/user/admin/dashboard/'
            else:
                return '/user/developer/dashboard/'
            
def sendMail(request):
    subject = "welcome to Django"
    message = "hello Django"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [User.objects.values_list('email', flat=True)]
    res = send_mail(subject,message,email_from,recipient_list)
    if res>=0:
        print("mail sent")
    else:
        print("mail not sent")
    print(res)
    return HttpResponse("mail sent")


def logoutUser(request):
    logout(request)
    return redirect('/user/login/')
            
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  Dashboard View

# @method_decorator(login_required(login_url='/user/login/'),name='dispatch')
@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class AdminDashboardView(TemplateView):

    template_name="user/admin_dashboard.html"



# @method_decorator([login_required(login_url='/user/login/'),manager_required],name='dispatch')
class ManagerDashBoardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()    

        return render(request, 'user/manager_dashboard.html',{'projects':project})

    template_name = 'user/manager_dashboard.html'


@method_decorator([login_required(login_url='/user/login/'),developer_required],name='dispatch')
class DeveloperDashBoardView(TemplateView):
    
    template_name= 'user/developer_dashboard.html'


        

    
    
    



    
         
