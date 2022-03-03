"""projet1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.urls import path

from hub.forms import StudentForm
from .views import CreateStudentForm, StudentListView, coach_List, homePage, student_Details, student_List,studentCreate

urlpatterns = [
    path('home/', homePage,name="home"),
    path('index/', student_List,name="student_list"),
    path('coach/', coach_List,name="coach"),
    path('st_details/<int:id>', student_Details,name="student_Details"),
    path('studentlist',StudentListView.as_view(),name="student_s"),
    path('add_student/',studentCreate,name="student_ls"),
    path('CreateStudentForm/',CreateStudentForm,name="student_sf"),
    # path('CreateStudentView/',StudentForm,name="student_v"),
]
