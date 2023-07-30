from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Faculty(models.Model):
    name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class FileModel(models.Model):
    file = models.FileField(upload_to='files/')
    description=models.TextField(null=True,max_length=300)
    title=models.CharField(null=True,max_length=20)
    tags=models.JSONField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    studentPublication=models.ManyToManyField(Student,null=True)
    facultyPublication=models.ManyToManyField(Faculty,null=True)
    def __str__(self):
        return self.title