from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects',ProjectViewSet,basename='projects')
router.register(r'tasks',TaskViewSet,basename='tasks')
router.register(r'comments',CommentViewSet,basename='comments')

'''urlpatterns = [
    
    path('projects/', ProjectAPIView.as_view()),
    path('tasks/',TaskAPIView.as_view())
    '
]'''
urlpatterns = [
]

urlpatterns += router.urls