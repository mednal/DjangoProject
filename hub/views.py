from ast import List
from  django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from hub.models import Coach, Student

# Create your views here.

class StudentListView(ListView):
 model=Student
 template_name="hub/index.html"
 paginate_by=5

def homePage(request):
    return HttpResponse("<h1>Ahla wa sahla ")

def student_List(request): 
    List =Student.objects.all()
    return render(

        request,
        'hub/index.html',
        {
            'list':List
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
            'list':List
        }

    )


    




