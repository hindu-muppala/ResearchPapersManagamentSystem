
import json
import logging
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import FileModel,Student,Faculty
from django.http import HttpResponse, JsonResponse
def home(request):
    return render(request,'base.html')
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})
def file_list(request):
    files = FileModel.objects.all()
    return render(request, 'file_list.html', {'files': files})
def login(request):
     return render(request,'loginpg.html')
def SignUp(request):
    return render(request,'signUp.html')
def createStudent(request):
    json_data={}
    if request.method == 'POST':
        # Get the JSON data from the request body
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'validation': 'Invalid JSON data'})
    name1=json_data.get('name')
    college1=json_data.get('college')
    email1=json_data.get('email')
    password1=json_data.get('password')
    for i in Student.objects.all():
        if i.email==email1:
            return JsonResponse({'validation': "False"})
    # I should set cookie
    Student(name=name1,password=password1,email=email1,college=college1).save()
    return JsonResponse({'validation': "True"})
def createFaculty(request):
    json_data={}
    if request.method == 'POST':
        # Get the JSON data from the request body
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'validation': 'Invalid JSON data'})
    name1=json_data.get('name')
    college1=json_data.get('college')
    email1=json_data.get('email')
    password1=json_data.get('password')
    for i in Faculty.objects.all():
        if i.email==email1:
            return JsonResponse({'validation': "False"})
    # I should set cookie
    Faculty(name=name1,password=password1,email=email1,college=college1).save()
    logger = logging.getLogger(__name__)
    logger.info(f"Phone number: {request.POST.get('name')}")
    return JsonResponse({'validation': "True"})
# to show the show page
def show(request):
    return render(request,'show.html')
def validateStudent(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    if email and password:
        for i in Student.objects.all():
            if i.email == email and i.password == password:
                return JsonResponse({'validation': True})

    return JsonResponse({'validation': False})
def validateFaculty(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    if email and password:
        for i in Faculty.objects.all():
            if i.email == email and i.password == password:
                return JsonResponse({'validation': True})

    return JsonResponse({'validation': False})