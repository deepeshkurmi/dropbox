from django.urls import path
from . import views

urlpatterns = [
    path('files/upload/', views.FileUploadAPIView.as_view()),
    path('files/<str:file_id>/', views.FileReadAPIView.as_view()),
    path('files/<str:file_id>/update/', views.FileUpdateAPIView.as_view()),
    path('files/<str:file_id>/delete/', views.FileDeleteAPIView.as_view()),
    path('files/', views.FileListAPIView.as_view()),
]
