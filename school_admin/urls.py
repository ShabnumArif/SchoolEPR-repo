from django.urls import path
from . import views
urlpatterns=[
    path('home',views.school_home),
    path('add-staff',views.add_staff),
    path('view-student',views.view_student),
    path('view-staff',views.view_staff),
]