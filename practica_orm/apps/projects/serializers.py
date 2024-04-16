from rest_framework import serializers
from .models import *

class ProjectSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate_content(self,value):
        control_parent = ["hijueputa","hp","malparido","gonorrea"]
        for word in control_parent:
            if word in value.lower():
                raise serializers.ValidationError("The word word can not be in the comment task")
        return value
    
class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 60)
    init_date = serializers.DateTimeField(required = False)
    end_date = serializers.DateTimeField()

    def validate_name (self,value):
        if ("sair" in value):
            raise serializers.ValidationError("The name sair can not be in the project name")
        return value
    '''
    def validate_end_date (self, value):
        print(f'El tipo del validate_end_date: {type(value)}')
        return value
    '''
    def validate(self, attrs):
        print(attrs)

        return super().validate(attrs)

    def create(self, validated_data):
        Project(**validated_data).save()
        return self.data