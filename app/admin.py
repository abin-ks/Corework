from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Core Application'

class user_registration_view(admin.ModelAdmin):
    model = user_registration
    

class extracurricular_view(admin.ModelAdmin):
    model = extracurricular
    list_display=['user',]
    

class qualification_view(admin.ModelAdmin):
    model = qualification
    


class branch_registration_view(admin.ModelAdmin):
    model = branch_registration

class designation_view(admin.ModelAdmin):
    model = designation

class department_view(admin.ModelAdmin):
    model = department

class project_view(admin.ModelAdmin):
    model = project

class test_status_view(admin.ModelAdmin):
    model = test_status

class project_taskassign_view(admin.ModelAdmin):
    model = project_taskassign

class tester_status_view(admin.ModelAdmin):
    model = tester_status
class reported_issue_view(admin.ModelAdmin):
    model = reported_issue
class attendance_view(admin.ModelAdmin):
    model = attendance
class leave_view(admin.ModelAdmin):
    model = leave
class internship_view(admin.ModelAdmin):
    model = internship
class create_team_view(admin.ModelAdmin):
    model = create_team
class trainer_task_view(admin.ModelAdmin):
    model = trainer_task
class topic_view(admin.ModelAdmin):
    model = topic

   

admin.site.register(user_registration, user_registration_view)
admin.site.register(extracurricular, extracurricular_view)
admin.site.register(qualification, qualification_view)
admin.site.register(branch_registration, branch_registration_view) 
admin.site.register(designation, designation_view)
admin.site.register(department, department_view)
admin.site.register(project, project_view)
admin.site.register(test_status, test_status_view)
admin.site.register(project_taskassign, project_taskassign_view)
admin.site.register(tester_status, tester_status_view)
admin.site.register(reported_issue, reported_issue_view)
admin.site.register(attendance, attendance_view)
admin.site.register(leave, leave_view)
admin.site.register(internship, internship_view)
admin.site.register(create_team, create_team_view)
admin.site.register(trainer_task, trainer_task_view)
admin.site.register(topic, topic_view)
