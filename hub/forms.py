from  django import forms

from .models import Student 






class StudentModelForm(forms.Form):

    class Meta:
          model=Student
          fields="__all__" #['last_name'] 


class StudentForm (forms.Form): 
    first_name=forms.CharField(

        label='Prenom',

    ) 
    
    last_name=forms.CharField(

        label='nom',
        max_length=50
    )

    email=forms.EmailField(

        label='email',
        max_length=50
    )


