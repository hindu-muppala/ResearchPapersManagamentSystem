
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import FileModel
# from .models import Candidate
# form .models import Student
def home(request):
    return render()
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
     return render('loginpg.html')
def SignUp(request):
    return render(request,'signUp.html')
def createStudent(request):
    if request.method== 'POST':
        pass
def createFaculty(request):
    if request.method== 'POST':
        pass
def dashboard(request):
    pass