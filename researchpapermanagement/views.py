
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import FileModel
# from .models import Candidate
# form .models import Student
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
def SignUp(request):
    return render(request,'signUp.html')
def createUser(request):
    if request.method== 'POST':
        pass
    