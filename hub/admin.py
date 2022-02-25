from email import message
from inspect import Parameter
import numbers
from sqlite3 import Row
from urllib import request
from django.contrib import admin,messages
from .models import *
# Register your models here.
def set_Valid (modeladmin,request,querset):
    rows =querset.update(isValid=True)
    if rows:
       msg="1 project was"
   
    else:
      msg=f"{rows}projects were"

    messages.success(request,message=f"{msg} succesfully")



class ProjectDurationField(admin.SimpleListFilter):
    parameter_name="dure"
    title="Durée"
    

    def lookups(self, request, model_admin ) :
        return (
                ('1 Month','less than 1'),
                ('3 Months','less than 3'),
                ('Months greater than 3','greater than 9')
   
               )
     
    def queryset(self, request, queryset ):
        if self.value()=="1 Month":
            return queryset.filter(dure__lte=30)
          
        if self.value()=="3 Months":
            return queryset.filter(dure__gt=30,dure__lte=90)   
        if self.value()=="Months greater than 3":
            return  queryset.filter(dure__gt=90)   

class ProjectInline(admin.StackedInline):
    model=Projet


class ProjectAdmin(admin.ModelAdmin): 
 def set_InValid (modeladmin,request,querset):
      number=querset.filter(isValid=False)
      if number.count()>0:
          message.error(request,"aaaaaaaaaa")  

 actions={set_Valid,'set_InValid'}
 
 actions_on_bottom=True
 actions_on_top=True
 list_filter=(
        'creator',
        'isValid',
        ProjectDurationField
    )
    
 list_display=(
            'project_name',
            'dure',
            'isValid'
           
        )
        

 fieldsets=[
                (
                    'state',  
                    {
                        'fields':('isValid',)
                    } 
                ),
                (
                    'About',
                    {
                    
                        'fields':(
                        'project_name',
                        ('creator','supervisor','dure','description','temp_allocated'),
                        )
                
                    }
                )

    ]

class StudentAdmin(admin.ModelAdmin):
    list_display=(
    'first_name',
    'last_name'
        )
    fields=(
    ('first_name','last_name'),
    'email'

    )
   
    search_fields=['last_name','first_name']
    
    inlines=[ProjectInline]
admin.site.register([MemberShip])
admin.site.register(Student,StudentAdmin)
admin.site.register(Coach,StudentAdmin)
admin.site.register(Projet,ProjectAdmin)
