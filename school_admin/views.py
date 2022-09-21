from django.shortcuts import render                                                                                                                                                                                                                                                                                                

# Create your views here.
def school_home(request):
    return render(request,'school_admin_templates/home.html')
