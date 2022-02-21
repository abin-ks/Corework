from django.urls import re_path,include
from .import views


urlpatterns = [
    re_path(r'^$', views.login, name="login"),
    re_path(r'^home$', views.home, name='home'),
    re_path(r'^devindex$', views.devindex, name='devindex'),
    re_path(r'^devdashboard$', views.devdashboard, name='devdashboard'),
    re_path(r'^devReportedissues$', views.devReportedissues, name='devReportedissues'),
    re_path(r'^devreportissue$', views.devreportissue, name='devreportissue'),
    re_path(r'^devreportedissue$', views.devreportedissue, name='devreportedissue'),
    re_path(r'^devsuccess$', views.devsuccess, name='devsuccess'),
    re_path(r'^devissues$', views.devissues, name='devissues'),
    re_path(r'^dev_leave_form$', views.dev_leave_form, name='dev_leave_form'),
    


    re_path(r'^Devapplyleav$', views.Devapplyleav, name='assigned'),
    re_path(r'^Devapplyleav1$', views.Devapplyleav1, name='dashboard'),
    re_path(r'^Devapplyleav2$', views.Devapplyleav2, name='project'),
    re_path(r'^Devleaverequiest$', views.Devleaverequiest, name='projectdetails'),
    re_path(r'^Devattendance$', views.Devattendance, name='submitted'),
    re_path(r'^Devattend$', views.Devattend, name='Devattend'),
    re_path(r'^Devapplyleav3$', views.Devapplyleav3, name='task'),



    re_path(r'^DEVprojects$', views.DEVprojects, name='DEVprojects'),
    re_path(r'^DEVsuccess$', views.DEVsuccess, name='DEVsuccess'),
    re_path(r'^DEVtable$', views.DEVtable, name='DEVtable'),
    re_path(r'^DEVtask$', views.DEVtask, name='DEVtask'),
    re_path(r'^DEVtaskform$', views.DEVtaskform, name='DEVtaskform'),
    re_path(r'^DEVtaskmain$', views.DEVtaskmain, name='DEVtaskmain'),
    re_path(r'^dev_task_submit$', views.dev_task_submit, name='dev_task_submit'),
    re_path(r'^DEVtaskformsubmit$', views.DEVtaskformsubmit, name='DEVtaskformsubmit'),
    re_path(r'^DEVtasksumitted$', views.DEVtasksumitted, name='DEVtasksumitted'),
    


    re_path(r'^TSassigned$', views.TSassigned, name='TSassigned'),
    re_path(r'^TSdashboard$', views.TSdashboard, name='TSdashboard'),
    re_path(r'^TSproject$', views.TSproject, name='TSproject'),
    re_path(r'^TSprojectdetails$', views.TSprojectdetails, name='TSprojectdetails'),
    re_path(r'^TSsubmitted$', views.TSsubmitted, name='TSsubmitted'),
    re_path(r'^TStask$', views.TStask, name='TStask'),
    re_path(r'^TSsucess$', views.TSsucess, name='TSsucess'),


    # amal
    #re_path(r'^$', views.index, name='index'),
    re_path(r'^tldashboard$', views.tldashboard, name='tldashboard'),
    re_path(r'^tlprojects$', views.tlprojects, name='tlprojects'),
    re_path(r'^tlprojecttasks$', views.tlprojecttasks, name='tlprojecttasks'),
    re_path(r'^tlsplittask$', views.tlsplittask, name='tlsplittask'),
    re_path(r'^tlgivetask$', views.tlgivetask, name='tlgivetask'),
    # abin
    re_path(r'^TLattendance$', views.TLattendance, name='TLattendance'),
    re_path(r'^TLreportissues$', views.TLreportissues, name='TLreportissues'),
    re_path(r'^TLreportedissue1$', views.TLreportedissue1, name='TLreportedissue1'),
    re_path(r'^TLreportedissue2$', views.TLreportedissue2, name='TLreportedissue2'),
    re_path(r'^TLreport1$', views.TLreport1, name='TLreport1'),
    re_path(r'^TLreportsuccess$', views.TLreportsuccess, name='TLreportsuccess'),
    # bibn
    re_path(r'^TLtasks$', views.TLtasks, name='TLtasks'),
    re_path(r'^TLleave$', views.TLleave, name='TLleave'),
    re_path(r'^TLleavereq$', views.TLleavereq, name='TLleavereq'),
    re_path(r'^TLreqedleave$', views.TLreqedleave, name='TLreqedleave'),
    re_path(r'^TLgivetasks$', views.TLgivetasks, name='TLgivetasks'),
    re_path(r'^TLgavetask$', views.TLgavetask, name='TLgavetask'),
    re_path(r'^TLsuccess$', views.TLsuccess, name='TLsuccess'),


    # project manager module

    re_path(r'^pmanager_dash', views.pmanager_dash,name="pmanager_dash"),
    re_path(r'^projectmanager_projects', views.projectmanager_projects, name="projectmanager_projects"),

    #nirmal
    re_path(r'^projectmanager_assignproject', views.projectmanager_assignproject, name="projectmanager_assignproject"),

    #jensin
    re_path(r'^projectmanager_createproject', views.projectmanager_createproject, name="projectmanager_createproject"),

    #maneesh
    re_path(r'^projectmanager_description', views.projectmanager_description, name="projectmanager_description"),
    re_path(r'^projectmanager_table', views.projectmanager_table, name="projectmanager_table"),
    re_path(r'^projectmanager_upprojects', views.projectmanager_upprojects, name="projectmanager_upprojects"),

    #praveesh
    re_path(r'^projectmanager_accepted_projects', views.projectmanager_accepted_projects, name="projectmanager_accepted_projects"),
    re_path(r'^projectmanager_rejected_projects', views.projectmanager_rejected_projects, name="projectmanager_rejected_projects"),



    #amal#bibin#rohit#abin
    re_path(r'^manindex$', views.manindex, name='manindex'),
    re_path(r'^projectmanEmp$', views.projectmanEmp, name='projectmanEmp'),
    re_path(r'^projectmanDev$', views.projectmanDev, name='projectmanDev'),
    re_path(r'^projectmanDevDashboard$', views.projectmanDevDashboard, name='projectmanDevDashboard'),
    re_path(r'^projectman_developer_attendance$', views.projectman_developer_attendance, name='projectman_developer_attendance'),

    re_path(r'^projectman_team$', views.projectman_team, name='projectman_team'),
    re_path(r'^projectman_team_profile$', views.projectman_team_profile, name='projectman_team_profile'),
    re_path(r'^projectman_team_attendance$', views.projectman_team_attendance, name='projectman_team_attendance'),

    re_path(r'^projectMANattendance$', views.projectMANattendance, name='projectMANattendance'),
    re_path(r'^projectMANreportedissues$', views.projectMANreportedissues, name='projectMANreportedissues'),
    re_path(r'^projectMANreportedissue$', views.projectMANreportedissue, name='projectMANreportedissue'),
    re_path(r'^projectMANreportissue$', views.projectMANreportissue, name='projectMANreportissue'),
    re_path(r'^projectmanagerreportedissue2$', views.projectmanagerreportedissue2, name='projectmanagerreportedissue2'),
    re_path(r'^MANreportsuccess$', views.MANreportsuccess, name='MANreportsuccess'),
    re_path(r'^projectMANleave$', views.projectMANleave, name='projectMANleave'),
    re_path(r'^projectMANleavereq$', views.projectMANleavereq, name='projectMANleavereq'),
    re_path(r'^projectMANreqedleave$', views.projectMANreqedleave, name='projectMANreqedleave'),

    re_path(r'^Manager_employees$', views.Manager_employees, name='Manager_employees'),
    re_path(r'^projectManager_tl$', views.projectManager_tl, name='projectManager_tl'),
    re_path(r'^projectManager_tl_dashboard$', views.projectManager_tl_dashboard, name='projectManager_tl_dashboard'),
    re_path(r'^man_tl_attendance$', views.man_tl_attendance, name='man_tl_attendance'), 

    re_path(r'^projectmanager_currentproject$', views.projectmanager_currentproject, name='projectmanager_currentproject'), 
    re_path(r'^projectmanager_currentdetail$', views.projectmanager_currentdetail, name='projectmanager_currentdetail'), 
    re_path(r'^projectmanager_currentteam$', views.projectmanager_currentteam, name='projectmanager_currentteam'),
    re_path(r'^projectmanager_completeproject$', views.projectmanager_completeproject, name='projectmanager_completeproject'),
    re_path(r'^projectmanager_completedetail$', views.projectmanager_completedetail, name='projectmanager_completedetail'), 
    re_path(r'^projectmanager_completeteam$', views.projectmanager_completeteam, name='projectmanager_completeteam'),
    re_path(r'^projectmanager_teaminvolved$', views.projectmanager_teaminvolved, name='projectmanager_teaminvolved'),
    re_path(r'^projectmanager_devteam$', views.projectmanager_devteam, name='projectmanager_devteam'),


    re_path(r'^projectmanager_currenttl$', views.projectmanager_currenttl, name='projectmanager_currenttl'),
    re_path(r'^projectmanager_completetl$', views.projectmanager_completetl, name='projectmanager_completetl'),
    re_path(r'^projectmanager_tlreported$', views.projectmanager_tlreported, name='projectmanager_tlreported'), 


]