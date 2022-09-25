from django.urls import path
from . import views

urlpatterns = [
    path('add-student',views.add_student),
    path('change-password',views.change_password),
    path('teacher-home',views.teacher_home) ,
    path('view-student', views.view_student),   
]
