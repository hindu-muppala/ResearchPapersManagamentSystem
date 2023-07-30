from django.urls import path
from . import views
urlpatterns = [
   
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('',views.home),
    path('logIn',views.login),
    path('signUp',views.SignUp),
    path('createStudent',views.createStudent),
    path('createFaculty',views.createFaculty),
    path('validStudent',views.validateStudent),
    path('validFaculty',views.validateFaculty),
    path('dashboard',views.show)
]