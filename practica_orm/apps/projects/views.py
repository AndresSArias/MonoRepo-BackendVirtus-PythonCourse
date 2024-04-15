from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .models import *
# Create your views here.
class ProjectAPIView(APIView):
    def get(self,request):
        projects = Project.objects.all()
        data = [
            {
                "id" :project.id,
                "name": project.name,
            }
            for project in projects
        ]
        return Response(data)
    

    def post(self,request):
        print(request.data)

        project = Project()

        project.name = request.data.get('name',"")
        project.init_date = datetime.now()

        end_date = request.data.get('end_date',"")
        project.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')

        project.save()

        return Response({})
