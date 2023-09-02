from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class ProjectCreationView(CreateView):
    form_class = ProjectCreationForm
    model = Project
    template_name= 'project/project_create.html'
    success_url='/project/list_project/'


    def form_valid(self, form):
        return super().form_valid(form)

    
class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return super().get_queryset()
    

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_update.html'
    success_url='/project/list_project/'

class ProjectDetailView(DetailView):
    model = Project
    template_name= 'project/project_detail.html'
    context_object_name = 'project_detail'

    labels = []
    data = []
    project = Project.objects.all().values_list('title', flat=True)
    time = Project.objects.all().values_list('estimatedHours', flat=True)
    for i in project:
        labels.append(i)
    for i in time:
        data.append(i)

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id=self.kwargs['pk'])
        return render(request, self.template_name, {'project_detail':self.get_object(),'team':team, 'labels':self.labels, 'data':self.data})
    
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/project_delete.html"
    success_url= '/project/list_project/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class Create_Project_Team(CreateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project/'

    def form_valid(self, form):
        return super().form_valid(form)

class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'

class ProjectTeamByProject(ListView):
    model = ProjectTeam
    template_name= 'project/project_team_list.html'
    context_object_name = 'project_team_list'

    def get_queryset(self):
        return super().get_queryset().filter(project_id=self.kwargs['pk'])
    
# Project Module

class CreateProjectModule(CreateView):
    form_class = ProjectModuleCreationForm
    model = ProjectModule
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'

class ProjectModuleList(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'

class ProjectModuleListByProject(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'  
    context_object_name = 'project_module_list'

    def get_queryset(self):
        return super().get_queryset().filter(project_id = self.kwargs['pk'])

class CreateProjectTaskView(CreateView):
    model = ProjectTask
    form_class = CreateProjectTaskForm
    template_name = 'project/project_task_create.html'
    success_url = '/project/list_project_task/'

class ModuleDetailView(DetailView):
    model = ProjectModule
    template_name = 'project/project_module_detail.html'

    def get(self, request, *args, **kwargs):
        module = ProjectModule.objects.filter(id=self.kwargs['pk']).values()
        projectTask = ProjectTask.objects.filter(module_id = self.kwargs['pk']).values()
        print('.......',projectTask)
        print('.......',module)
        return render(request,self.template_name,{'module_detail':module,'projectTask':projectTask}) 
    

