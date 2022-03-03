from pyexpat import model
from  django.views.generic import ListView,CreateView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from hub.forms import StudentForm, StudentModelForm
from hub.models import Coach, Student


# Create your views here.

class StudentListView(ListView):


 
 model=Student
 template_name="hub/index.html"
 paginate_by=5





def studentCreate (request):
    print(request)
    if request.method =='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
    return render(
            request,
            'hub/add_student.html'
        )

def homePage(request):
    return HttpResponse("<h1>Ahla wa sahla")
    

def student_List(request): 
    List =Student.objects.all()
    return render(

        request,
        'hub/index.html',
        {
            'students':List
        }
    )

   
def student_Details(request,id): 
 student = Student.objects.get(id=id)   
 return render(

        request,
        'hub/st_details.html',
        {
            'students':student
        }
    ) 



def coach_List(request): 
    List =Coach.objects.all()
    return render(

        request,
        'hub/index.html',
        {
            'students':List
        }

    )
 #     Student.objects.create(

        #          first_name=form.cleaned_data.get('first_name'),
        #          last_name=form.cleaned_data.get('last_name'),
        #          email=form.cleaned_data.get('email')
        # )


def CreateStudentForm(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
    return render(
        request,
        'hub/add_student.html',
        {
            'form': form,
        }

    )


def add_student(request):
    form =StudentModelForm()
    if request.method=='POST':
        form =StudentModelForm(request.POST)
        if form.is_valid():
            student=form.save(commit=False)
            Student.save()
            return redirect('Student_list')
    return render(
        request,
        'hub/add_student.html',
        {
            'form':form
        }
    )


class StudentCreatView(CreateView):
    model=Student
    from_class=StudentModelForm
    def get_success_url(self):
        return redirect('studentlist')





