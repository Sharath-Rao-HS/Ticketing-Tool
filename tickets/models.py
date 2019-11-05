from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class project(models.Model):
    projectName = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    client = models.CharField(max_length=100)
    managerName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.projectName } - {self.id}'



class Employee(models.Model):
    EmployeeName = models.CharField(max_length=100)
    project = models.ForeignKey(project, on_delete=models.SET_NULL, null = True)
    
    def __str__(self):
        return self.EmployeeName


class ticketHeader(models.Model):
    
    title = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    Employee = models.ForeignKey(Employee, on_delete=models.SET_NULL,null = True)
    Tickettype = models.CharField(max_length=100,null = True)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=600)
    attachment = models.FileField(null=True)
    creater = models.ForeignKey(User, on_delete=models.SET_NULL,null = True)
    project = models.ForeignKey(project,on_delete=models.SET_NULL,null = True)

    def __str__(self):
        return self.title


class ticketlog(models.Model):
    ticketid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    Employee = models.ForeignKey(Employee, on_delete=models.SET_NULL,null = True)
    Tickettype = models.CharField(max_length=100,null=True)
    Ticketsubtype = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=600,null=True)
    attachment = models.FileField(null=True)
    project = models.ForeignKey(project,on_delete=models.SET_NULL,null = True)

    def __str__(self):
        return self.title