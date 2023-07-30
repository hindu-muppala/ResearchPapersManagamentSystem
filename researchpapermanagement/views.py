
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import FileModel,Student,Faculty
from django.http import HttpResponse
# from .models import Candidate
# form .models import Student
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
    pass
def createFaculty(request):
    return HttpResponse(request.GET)
def dashboard(request):
    pass