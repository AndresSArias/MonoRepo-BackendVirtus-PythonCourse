from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from .models import *
from .serializers import *

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerModel

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# Create your views here.
class ProjectAPIView(APIView):
    def get(self,request):
        projects = Project.objects.all()
        '''        
        data = [
            {
                "id" :project.id,
                "name": project.name,
            }
            for project in projects
        ]
        return Response(data)
        '''
        serializer = ProjectSerializer(projects,many = True)

        return Response(serializer.data)
    

    def post(self,request):
        project = Project()
        '''
        print(request.data)

        

        project.name = request.data.get('name',"")
        project.init_date = datetime.now()

        end_date = request.data.get('end_date',"")
        project.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')

        project.save()

        
        '''        
        serializer = ProjectSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})





    
    def delete (self,request):
        id = request.data.get("id")
        #Get de ORM
        project = Project.objects.get(id = id)
        
        project.delete()

        return Response({})
    
    def patch(self,request):
        id = request.data.get("id")
        project = Project.objects.get(id = id)

        project.name = request.data.get("name",project.name)

        project.save()

        return Response ({

            "id": id,
            "new_name": Project.objects.get(id = id).name

        })

class TaskAPIView(APIView):

    def get(self,request):
        tasks = Task.objects.all()
        data = [
            {
                "id" :task.id,
                "project": task.project.name,
                "desc": task.description,
                "priority": task.priority,
            }
            for task in tasks
        ]
        return Response(data)
    
    def post(self,request):

        task = Task()

        id_project = request.data.get('id_project',"")

        task.project = Project.objects.get(id = id_project)

        task.description = request.data.get('Desc','No desc.')
        task.priority = request.data.get('Priority', 9)

        end_date = request.data.get('end_date',"")
        task.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')

        task.save()

        return Response({})    
        
    def delete (self,request):
        id = request.data.get("id")
        #Get de ORM
        task = Task.objects.get(id = id)
        
        task.delete()

        return Response({})        
    
    def patch(self,request):
        id = request.data.get("id")
        task = Task.objects.get(id = id)

        task.priority = request.data.get("new_priority",task.priority)

        task.save()

        return Response ({

            "id": id,
            "project": Task.objects.get(id = id).project.name,
            "desc": Task.objects.get(id = id).description,
            "new_priority": Task.objects.get(id = id).priority,            

        })    