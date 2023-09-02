from django.db import models
from user.models import * 

# Create your models here.

technology_choice = (('django','Django'),
                     ('spring','Spring'),
                     ('mern','Mern'),
                     ('mean','Mean'),
                     ('php','PHP'))


# Project Class
status_choice = (('Completed','Completed'), 
                 ('Pending','Pending'), 
                 ('Cancelled','Cancelled'))

class Project(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True) 
    technology = models.CharField(choices=technology_choice,max_length=100)
    estimatedHours = models.PositiveIntegerField()
    startDate = models.DateField()
    completionDate = models.DateField()
    status = models.CharField(choices=status_choice,max_length=100,default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project'
    
    def __str__(self):
        return self.title

#  ProjectTeam class

class ProjectTeam(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #

    class Meta:
        db_table = 'Project_Team'

status_choice = (('Completed','Completed'), 
                 ('Pending','Pending'), 
                 ('Cancelled','Cancelled'))

# Status Class

class Status(models.Model):

    statusName = models.CharField(choices=status_choice ,max_length=20) 
    
    class Meta:
        db_table = 'status'
    
    def __str__(self):
        return self.statusName

# ProjectModule Class

status_choice = (('Completed','Completed'), 
                 ('Pending','Pending'), 
                 ('Cancelled','Cancelled'))

class ProjectModule(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    estimatedHours = models.IntegerField()
    status = models.CharField(choices=status_choice, max_length=100)
    startDate = models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Project_Module'
    
    def __str__(self):
        return self.moduleName

priority_choice = (('low','Low'),
                   ('medium','Medium'),
                   ('high','High'))

# Task Class

class ProjectTask(models.Model):
    
    module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=100)
    description = models.TextField()
    estimeted_hours = models.IntegerField()
    status = models.CharField(choices =status_choice,max_length=100)
    startDate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ProjectTask'
    
    def __str__(self):
        return self.taskName

# UserTask Class

class UserTask(models.Model): 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(ProjectTask, on_delete=models.CASCADE)

    class Meta:
        db_table = 'User_Task'
        