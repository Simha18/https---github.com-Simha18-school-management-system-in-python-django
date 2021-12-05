from django.contrib import admin
from admissions.models import Student
from admissions.models import Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','exp','contact']

# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
