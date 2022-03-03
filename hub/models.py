from audioop import reverse
from django.db import models
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
# Create your models here.



def is_Nalouti_Email(value):
    if not str(value).endswith('@nalouti.tn'):

        raise ValidationError('Your mail must end with @nalouti.tn',
            params={'value':value}
        )
    return value


class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(validators=[is_Nalouti_Email]) #de base Chrafield
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Student(User):

    def get_absolute_url(self):
        return reverse('Student_list')
    
    pass
class Coach(User):
    pass
class Projet(models.Model):
    project_name=models.CharField(max_length=50)
    dure=models.IntegerField()
    temp_allocated=models.IntegerField(validators=[MinValueValidator(2,"le temps min doit etre 5 heure"),
    MaxValueValidator(5,"Max Value should be inferior to 5")])
    besoin=models.TextField(max_length=250)
    description=models.TextField(max_length=250)
    isValid=models.BooleanField(default=False)
    creator=models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='creators'
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.CASCADE, #en cas ou en supprime le user ,l'attribut va etre null
        related_name='supervisors'
    )
    member=models.ManyToManyField(
        Student,
        through='MemberShip' ,
        related_name='membres'   
    ) #il va genere une classe intermidiare nommé membreShip
    def __str__(self) -> str:
        return f"{self.project_name}"
class MemberShip(models.Model):
    projet=models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
    )
    allocated_time_by_member=models.IntegerField(default=0)