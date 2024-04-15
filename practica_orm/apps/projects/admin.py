from django.contrib import admin
from .models import *

# Register your models here.
class ProjectsAdmin (admin.ModelAdmin):
    list_display = ["name", "init_date","end_date"]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "project","priority","description","end_date"]    

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","task","content","init_date"]

class MemberAdmin(admin.ModelAdmin):
    list_display = ["user","role","project"]

class OwnerAdmin(admin.ModelAdmin):
    list_display = ["user","task"]

admin.site.register(Project,ProjectsAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Owner,OwnerAdmin)