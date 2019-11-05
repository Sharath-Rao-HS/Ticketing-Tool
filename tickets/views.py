from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from tickets.models import *
from pprint import pprint
from django.conf import settings  
from django.http import JsonResponse
# Create your views here.
def createTicket(request,projectid):

    if request.method == "POST":
        module = request.POST.get('module')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        asign = request.POST.get('asign')
        employee = Employee.objects.get(id = asign)
        task = request.POST.get('task')
        print(status)
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        attachment = request.FILES['attachment']
        project1  = project.objects.get(id = int(projectid))
        ticket = ticketHeader.objects.create(
            title = title,
            module = module,
            priority = priority,
            status = status,
            Employee = employee,
            Tickettype = task,
            comments = summary,
            attachment = attachment,
            project = project1,
        )
        print(ticket)
        ticket = ticketlog.objects.create(
            ticketid = ticket.id,
            title = title,
            module = module,
            priority = priority,
            status = status,
            Employee = employee,
            Tickettype = task,
            comments = summary,
            attachment = attachment,
            project = project1,
        )
        project1 = project.objects.get(id=1)
        ticketHead = ticketHeader.objects.filter(project = project1)
        return render(request,'home.html',{
            'ticketHead':ticketHead,
            'project':project1,
        })

    project1 = project.objects.get(id = projectid)
    print(project1.id)
    return render(request,'create.html',{
        'project':project1,
    })

def employeelist(request,projectid):
    Employee1 = list(Employee.objects.filter(project = projectid ).values())
    return JsonResponse(Employee1, safe=False)


def viewticket(request,ticketid):
    if request.method == "POST":
        ticket = ticketHeader.objects.get(id = ticketid)
        module = request.POST.get('module')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        # asign = request.POST.get('asign')
        # print('asign',asign)
        # employee = Employee.objects.filter(id = asign)
        task = request.POST.get('task')
        print('status',status)
        title = request.POST.get('title')
        print(title)
        summary = request.POST.get('summary')
        # attachment = request.FILES['attachment']
        print('project',ticket.project.id)
        project1  = project.objects.get(id = ticket.project.id)
        ticket.status = status
        ticket.priority = priority
        ticket.comments = summary
        ticket.save()
        ticketlg = ticketlog.objects.create(
            ticketid = ticket.id,
            title = ticket.title,
            module = ticket.module,
            priority = priority,
            status = status,
            Employee = ticket.Employee,
            Tickettype = ticket.Tickettype,
            comments = summary,
            # attachment = attachment,
            project = project1,
        )
        return render(request,'view.html',{
        'ticket':ticket,
        'project':project1,
        'employee':ticket.Employee,
        })

    ticket = ticketHeader.objects.get(id = ticketid)
    project1 = project.objects.get(id = ticket.project.id)
    return render(request,'view.html',{
        'ticket':ticket,
        'project':project1,
        'employee':ticket.Employee,
    })
    

def log(request,ticketID):
    ticketHead = ticketHeader.objects.get(id = ticketID)
    ticketlogs = ticketlog.objects.filter(ticketid = ticketID)
    project1 = project.objects.get(id = ticketHead.project.id)
    return render(request,'log.html',{
        'ticketHead':ticketHead,
        'ticketlogs':ticketlogs,
        'project':project1
    })

def home(request):
    project1 = project.objects.get(id=1)
    ticketHead = ticketHeader.objects.filter(project = project1)
    return render(request,'home.html',{
        'ticketHead':ticketHead,
        'project':project1,
    })
    

def projectticket(request):
    # hotel_id = request.session['hotel_id'] 
    # itemlist = menulist.objects.filter(hotelid = hotel_id)
    lables = ['Low','Medium','High']
    dataset = []
    datasetsum = []
    
    tablelow = ticketHeader.objects.filter(priority='Low')
    tablemedium = ticketHeader.objects.filter(priority='Medium')
    tablehign = ticketHeader.objects.filter(priority='High')

    dataset.append(len(tablelow))
    dataset.append(len(tablemedium))
    dataset.append(len(tablehign))

    table1 = ticketHeader.objects.filter(status='Open')
    table2 = ticketHeader.objects.filter(status='work in progress')
    table3 = ticketHeader.objects.filter(status='pending from customer side')
    table4 = ticketHeader.objects.filter(status='solution Proposed')
    table5 = ticketHeader.objects.filter(status='closed')
    lableslist = ['Open','work in progress','pending from customer side','solution Proposed','closed']
    datasetsum.append(len(table1))
    datasetsum.append(len(table2))
    datasetsum.append(len(table3))
    datasetsum.append(len(table4))
    datasetsum.append(len(table5))
   

    print(dataset,lables)
    data = {
        "lables":lables,
        "dataset":dataset,
        "lableslist":lableslist,
        "datasetsum":datasetsum,
    }
    return JsonResponse(data)    