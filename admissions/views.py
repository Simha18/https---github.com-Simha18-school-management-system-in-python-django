from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
#class based views
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.


# function based, class based views
@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

@login_required
def addAdmission(request):
    #values={"name":"Simha","age":28,"address":"Vizag"}
    form = StudentModelForm
    studentform = {'form':form}
    if request.method=='POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)


    return render(request, 'admissions/add-admission.html',studentform);


@login_required
@permission_required('admissions.view_student')
def admissionsReport(request):
    #get all records form the table
    result = Student.objects.all();   #SELeCT * form Stident
    #store it in dictionary
    students = {'allstudents':result}
    return render(request, 'admissions/admission-report.html',students);

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s = Student.objects.get(id=id) #select * from admissions_student where id=idvalue
    s.delete()
    return admissionsReport(request)

@login_required
@permission_required('admissions.change_student')  #4 actions, like add delete  change view these permission requests
def updateStudent(request,id):
    s = Student.objects.get(id=id) #select * from admissions_student where id=idvalue
    form = StudentModelForm(instance=s)
    dict = {'form':form}

    if request.method=='POST':
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return admissionsReport(request)


    return render(request,'admissions/update-admission.html',dict)

@login_required
def addVendor(request):
        #values={"name":"Simha","age":28,"address":"Vizag"}
        form = VendorForm
        vform = {'form':form}
        if request.method=='POST':
            form = VendorForm(request.POST)
            if form.is_valid():
                #form.save()   if not save
                n = (form.cleaned_data['name'])
                a = (form.cleaned_data['address'])
                c = (form.cleaned_data['contact'])
                i = (form.cleaned_data['item'])
                #dict = {"name":n,"address":a,"Contact":c,"item":i}
                #return homepage(request)
                #return homepage(request)
                response = render(request,'index.html');
                #response.set_cookie("name",n)    ---COOKIES SET
                #response.set_cookie("address",a)
                #response.set_cookie("contact",c)
                #response.set_cookie("item",i)
                #session set_cookie
                request.session['name']=n;
                request.session['address']=a;
                request.session['contact']=c;
                request.session['item']=i;

            return response


        return render(request, 'admissions/add-vendor.html',vform);


#Class Based Views like bellow


class FirstClassBasedView(View):
    def get(self,request):
       return HttpResponse("Hellow .. this first calss based view")


class TeacherRead(ListView):
    model = Teacher


class GetTeacher(DetailView):
    model = Teacher


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name','subject','exp','contact')


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name','subject','exp','contact')


class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')
