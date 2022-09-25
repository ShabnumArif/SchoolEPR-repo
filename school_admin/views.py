from django.shortcuts import render                                                                                                                                                                                                                                                                                                

# Create your views here.
def school_home(request):
    return render(request,'school_admin_templates/home.html')
def add_staff(request):
     return render(request,'school_admin_templates/add_staff.html')
def view_staff(request):
     return render(request,'school_admin_templates/view_staff.html')
def view_student(request):
     return render(request,'school_admin_templates/view_student.html')


