from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile),
    path('change-password',views.change_password),
    path('student-home',views.student_home) ,
]