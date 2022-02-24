from asyncio import Task
from tkinter import E, Variable
from django.http import request
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            pm = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
            request.session['pmid'] = pm.id
            return render(request, 'proman_sec.html', {'pm': pm})
        
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
           
            
            
            request.session['devid'] = member.id
            
            return render(request, 'DEVsec.html', {'member':member})
        
        else:
            context = {'msg': 'Invalid uname or password'}
            return render(request, 'login.html', context)


def devindex(request):
    return render(request, 'devindex.html')


def devdashboard(request):
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(fullname=devfn)
    return render(request, 'devdashboard.html', {'dev': dev})


def devReportedissues(request):
    return render(request, 'devReportedissues.html')


def devreportissue(request):
    return render(request, 'devreportissue.html')


def devreportedissue(request):
    
    if request.session.has_key('devdes'):
        devdes = request.session['devdes']
    if request.session.has_key('devdep'):
        devdep = request.session['devdep']
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    else:
        variable = "dummy"
    var=reported_issue.objects.all()
    vars=user_registration.objects.filter(fullname=devfn)
    
    return render(request,'devreportedissue.html',{'var':var,'vars':vars})



def devsuccess(request):
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    if request.method == 'POST':
        issue = request.POST.get("reportissue")
        vars = reported_issue(issue=issue)
        vars.save()
    return render(request, 'devsuccess.html')

def devissues(request):
    if request.session.has_key('devdes'):
        devdes = request.session['devdes']
    if request.session.has_key('devdep'):
        devdep = request.session['devdep']
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    vars=user_registration.objects.filter(fullname=devfn)
    var=reported_issue.objects.filter(reported_to_id=devid)
    return render(request,'devissues.html',{'vars':vars,'var':var})


def devsample(request):
    return render(request, 'devsample.html')


# *********************praveesh*********************


def Devapplyleav(request):
    return render(request, 'Devapplyleav.html')


def dev_leave_form(request):
    if request.method == "POST":
        leaves = leave()
        leaves.name = request.POST['name']
        leaves.branch = request.POST['branch']
        leaves.designation = request.POST['designation']
        leaves.from_date = request.POST['from']
        leaves.to_date = request.POST['to']
        leaves.leave_status = request.POST['haful']
        leaves.reason = request.POST['reason']
        leaves.user_id = request.POST['dev_id']
        leaves.status = "pending"
        leaves.save()
        return render(request, 'Devapplyleav.html')
    else:
        return render(request, 'Devapplyleav1.html')


def Devapplyleav1(request):
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(fullname=devfn)
    return render(request, 'Devapplyleav1.html', {'dev': dev})

def Devapplyleav2(request):
    return render(request, 'Devapplyleav2.html')


def Devleaverequiest(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = leave.objects.filter(user_id=devid)
    return render(request,'Devleaverequiest.html', {'dev': dev})

def Devattendance(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
 
    mem = user_registration.objects.filter(id=devid)
    
    return render(request, 'Devattendance.html',{'mem':mem})
    

def Devattend(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
 
    mem = user_registration.objects.filter(id=devid)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.raw('select id,date,status from app_attendance where date between "'+fromdate+'" and "'+todate+'"')
        
    return render(request, 'Devattendance.html',{'mem1':mem1,'mem':mem})

def Tattend(request):
    return render(request,'Tattend.html')
def Devapplyleav3(request):
    return render(request,'Devapplyleav3.html')



# **************************maneesh*********************


def DEVprojects(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        Variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    devs = projects
    return render(request,'DEVprojects.html')

def DEVtable(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    else:
        Variable = "dummy"
    projectid = request.GET.get('projectid')
    dev = user_registration.objects.filter(id=devid,fullname=devfn)
    time = datetime.now()
    devp = project_taskassign.objects.filter()
    return render(request, 'DEVtable.html',{'dev':dev,'devp':devp, 'time':time})

def DEVtablesave(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    
    return render(request, 'DEVtable.html')
    

def DEVtaskmain(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    task = trainer_task.objects.filter(user_id=devid)
    return render(request, 'DEVtaskmain.html', {'dev': dev, 'task': task})


def DEVtaskform(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    taskid = request.GET.get('taskid')
    time = datetime.now()
    dev = user_registration.objects.filter(id=devid)
    task = trainer_task.objects.filter(user_id=devid).filter(id=taskid)
    return render(request, 'DEVtaskform.html', {'dev': dev, 'task': task, 'time': time})

def DEVtaskformsubmit(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    if request.method == "POST":
        taskid = request.GET.get('taskid')
        task = trainer_task.objects.get(id=taskid)
        task.user_description = request.POST['description']
        task.user_files = request.FILES['scn']
        task.submissiondate = datetime.now()
        task.status = 'submitted'
        task.save()
    return render(request, 'DEVtasksumitted.html', {'dev': dev, 'task': task})

def DEVtask(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    taskid = request.GET.get('taskid')
    dev = user_registration.objects.filter(id=devid)
    task = trainer_task.objects.filter(user_id=devid).filter(id=taskid)
    return render(request, 'DEVtask.html', {'dev': dev, 'task': task})


def dev_task_submit(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    if request.method == "POST":
        dpid = request.POST.get('dpid')
        member = tester_status.objects.get(id=dpid)
        member.workdone=request.POST['workdone']
        member.save()
        return redirect('DEVtable')

def DEVtasksumitted(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVtasksumitted.html', {'dev': dev})
   
def DEVsuccess(request):
    return render(request,'DEVsuccess.html')



# **************************Rohit**************************


def TSdashboard(request):
    return render(request,'TSdashboard.html')
def TStask(request):
    return render(request,'TStask.html')
def TSproject(request):
    return render(request,'TSproject.html')
def TSprojectdetails(request):
    return render(request,'TSprojectdetails.html')
def TSassigned(request):
    return render(request,'TSassigned.html')
def TSsubmitted(request):
    return render(request,'TSsubmitted.html')
def TSsucess(request):
    return render(request,'TSsucess.html')


# ****************************amal*******************


def tldashboard(request):
    if request.session.has_key('usernametl'):
        usernameM1 = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernameM = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernameM2 = request.session['usernametl2']
    else:
        usernameM2 = "dummy"
    mem = user_registration.objects.filter(fullname=usernameM2)
    return render(request, 'TLdashboard.html' , {'mem':mem})
def tlprojects(request):
    return render(request, 'TLprojects.html')
def tlprojecttasks(request):
    return render(request, 'TLprojecttasks.html')
def tlsplittask(request):
    return render(request, 'TLsplittask.html')
def tlgivetask(request):
    return render(request, 'TLgivetask.html')


# **************************abin*************************


def TLattendance(request):
    return render(request, 'TLattendance.html')
def TLreportissues(request):
    return render(request, 'TLreportissues.html')
def TLreportedissue1(request):
    return render(request, 'TLreportedissue1.html')
def TLreportedissue2(request):
    return render(request, 'TLreportedissue2.html')
def TLreport1(request):
    return render(request, 'TLreport1.html')
def TLreportsuccess(request):
    return render(request, 'TLreportsuccess.html')


# ***********************bibin*****************************


def TLtasks(request):
    return render(request, 'TLtasks.html')
def TLleave(request):
    return render(request, 'TLleave.html')
def TLleavereq(request):
    return render(request, 'TLleavereq.html')
def TLreqedleave(request):
    return render(request, 'TLreqedleave.html')
def TLgivetasks(request):
    return render(request, 'TLgivetasks.html')
def TLgavetask(request):
    return render(request, 'TLgavetask.html')
def TLsuccess(request):
    return render(request, 'TLsuccess.html')



# project manager module
def promanagerindex(request):
    return render(request, 'promanagerindex.html')

def pmanager_dash(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
    else:
        variable = "dummy"
    member = user_registration.objects.filter(id=pmid)
    return render(request, 'pmanager_dash.html', {'member': member})

    

def projectmanager_projects(request):
    return render(request, 'projectmanager_projects.html')

# nirmal
def projectmanager_assignproject(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
    mem = user_registration.objects.filter(id=pmid)
    var = project.objects.filter(user_id=pmid)
    d = designation.objects.get(designation="TL")
    d1 = d.id
    spa = user_registration.objects.filter(projectmanager_id=pmid).filter(designation_id=d1)
    
    if request.session.has_key('pmid'):
            pmid = request.session['pmid']
    if request.method =='POST':
        
        var = project_taskassign()
        # print("hii")
        var.user_id = pmid
        var.tl_id = request.POST['pname']
        var.description=request.POST.get('desc')
        var.startdate=request.POST.get('sdate')
        var.enddate=request.POST.get('edate')
        var.files=request.POST.get('num')
        var.project_id = request.POST.get('yyy')
        print(var.project_id)
        # print(var.tl_id)
        var.save()
        return render(request, 'projectmanager_assignproject.html')
    

    return render(request, 'projectmanager_assignproject.html', {'var':var,'mem':mem,'spa':spa})

# jensin
def projectmanager_createproject(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
        mem = user_registration.objects.filter(id=pmid)
        
    if request.method =='POST':
        var = project()
        var.project=request.POST.get('pname')
        var.startdate=request.POST.get('sdate')
        var.enddate=request.POST.get('edate')
        var.description=request.POST.get('desc')
        var.files=request.POST.get('num')
        
        var.save()
    return render(request, 'projectmanager_createproject.html',{'mem':mem})

# maneesh
def projectmanager_description(request):
    return render(request, 'projectmanager_description.html')

def projectmanager_table(request):
    return render(request, 'projectmanager_table.html')

def projectmanager_upprojects(request):
    return render(request, 'projectmanager_upprojects.html')

# praveesh

def projectmanager_accepted_projects(request):
    return render(request, 'projectmanager_accepted_projects.html')

def projectmanager_rejected_projects(request):
    return render(request, 'projectmanager_rejected_projects.html')



# bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    return render(request, 'projectman_emp.html')

def projectmanDev(request):
    return render(request, 'projectman_dev.html')

def projectmanDevDashboard(request):
    return render(request, 'projectman_dev_Dashboard.html')

def projectman_developer_attendance(request):
    return render(request, 'projectman_developer_attendance.html')

def projectman_team(request):
    return render(request, 'projectman_team.html')

def projectman_team_profile(request):
    return render(request, 'projectman_team_profile.html')

def projectman_team_attendance(request):
    return render(request,'projectman_team_attendance.html')

def projectMANattendance(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
 
    mem = user_registration.objects.filter(id=pmid)
    
    return render(request, 'projectMANattendance.html',{'mem':mem})

def pmattend(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
 
    mem = user_registration.objects.filter(id=pmid)
    if request.method == "POST":
        
        pm = request.session['pmid']
       
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        
        # user = attendance.objects.filter(user_id=pmid)
        mem1 = attendance.objects.filter(date__range=[fromdate, todate])
        
      
    return render(request, 'projectMANattendance.html',{'mem1':mem1,'mem':mem})




def projectMANreportedissues(request):
    return render(request, 'projectMANreportedissues.html')

def projectMANreportedissue(request):
    return render(request, 'projectMANreportedissue.html')

def projectMANreportissue(request):
    return render(request, 'projectMANreportissue.html')

def projectmanagerreportedissue2(request):
    return render(request, 'projectmanagerreportedissue2.html')

def MANreportsuccess(request):
    return render(request, 'MANreportsuccess.html')

def projectMANleave(request):
    return render(request, 'projectMANleave.html')

def projectMANleavereq(request):
    return render(request, 'projectMANleavereq.html')

def projectMANreqedleave(request):
    return render(request, 'projectMANreqedleave.html') 

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    return render(request,'projectManager_tl.html')

def projectManager_tl_dashboard(request):
    return render(request,'projectManager_tl_dashboard.html')

def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')


def projectmanager_currentproject(request):
    return render(request, 'projectmanager_currentproject.html')

def projectmanager_currentdetail(request):
    return render(request, 'projectmanager_currentdetail.html')

def projectmanager_currentteam(request):
    return render(request, 'projectmanager_currentteam.html')

def projectmanager_completeproject(request):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
        asus = project.objects.all()
        
        
    return render(request, 'projectmanager_completeproject.html',{'asus':asus})

def projectmanager_completedetail(request,id):
    if request.session.has_key('pmid'):
        pmid = request.session['pmid']
    pro = user_registration.objects.filter(id=pmid)
    lost = project.objects.filter(id=id)
        
        
    return render(request, 'projectmanager_completedetail.html',{'lost':lost,'pro':pro})

def projectmanager_completeteam(request,id):
    if 'pmid' in request.session:
        if request.session.has_key('pmid'):
            pmid = request.session['pmid']
        else:
            pmid ="dummy"
        xmo = user_registration.objects.filter(id=pmid)
        p1 = designation.objects.get(designation="Developer")
        
        mem =user_registration.objects.filter(designation_id=p1).filter(TL_id=id)
    return render(request, 'projectmanager_completeteam.html',{'xmo':xmo,'mem':mem})

def projectmanager_teaminvolved(request):
    return render(request, 'projectmanager_teaminvolved.html')

def projectmanager_devteam(request):
    return render(request, 'projectmanager_devteam.html')

def projectmanager_currenttl(request):
   return render(request, 'projectmanager_currenttl.html')

def projectmanager_completetl(request):
    if 'pmid' in request.session:
        if request.session.has_key('pmid'):
            pmid = request.session['pmid']
        else:
            pmid ="dummy"
        man = user_registration.objects.filter(id=pmid)
        p1 = designation.objects.get(designation="TL")
        
        mem =user_registration.objects.filter(designation_id=p1)
    return render(request, 'projectmanager_completetl.html',{'man':man,'mem':mem})
    

def projectmanager_tlreported(request):
    return render(request, 'projectmanager_tlreported.html')
