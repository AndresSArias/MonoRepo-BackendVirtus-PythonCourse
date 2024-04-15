#libreria de los campos de un modelo
from django.db import models
from apps.users.models import User
# Create your models here.
#2. se crea el modelo con sus caracteristicas
class Project(models.Model):
    '''
    Campos utiles 
    '''
    name = models.CharField(max_length=60,null=False,blank=False)

    init_date = models.DateTimeField(null=False,blank=False)
    
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

def get_priority():
    return {i:i for i in range(10)}

class Task (models.Model):
    description = models.CharField(max_length=250)
    end_date = models.DateTimeField()
    priority = models.IntegerField(choices=get_priority)
    #Principal la foreingKey de donde viene y el tipo de eliminado
    project = models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.description


class Comment(models.Model):
    init_date = models.DateTimeField()
    content = models.CharField(max_length=120)
    task = models.ForeignKey(Task,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete= models.DO_NOTHING)

class Member(models.Model):
    
    ROLES = {
        "DEV": "DEVELOPER",
        "MAS": "SCRUM MASTER",
        "PRO": "PRODUCT OWNER"
    }
    
    date = models.DateField()
    role = models.CharField(max_length=3,choices=ROLES,default="DEV")

    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

class Owner (models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task,on_delete=models.DO_NOTHING)
