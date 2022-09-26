from django.shortcuts import render

# Create your views here.
def add_student(request):
     return render (request, 'teachers_templates/add_student.html')
def change_password(request):
     return render (request, 'teachers_templates/change_password.html')
def teacher_home(request):
     return render (request, 'teachers_templates/teacher_home.html')
def view_student(request):
     return render (request, 'teachers_templates/view_student.html')
     