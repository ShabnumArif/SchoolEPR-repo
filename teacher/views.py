from django.shortcuts import render

# Create your views here.
def add_student(request):
     return render (request, 'teacher_templates/add_student.html')
def change_password(request):
     return render (request,'teacher_templates/change_password.html')
def teacher_home(request):
     return render (request, 'teacher_templates/teacher_home.html')
def view_student(request):
     return render (request, 'teacher_templates/view_student.html')