from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    email=models.CharField()
    phno=models.CharField(max_length=10)
    password=models.IntegerField()
    def __str__(self):
        return self.name
class Faculty(models.Model):
    name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    email=models.CharField()
    phno=models.CharField(max_length=10)
    password=models.IntegerField()
    def __str__(self):
        return self.name
class FileModel(models.Model):
    file = models.FileField(upload_to='files/')
    description=models.TextField()
    title=models.CharField()
    tags=models.JSONField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    studentPublication=models.ManyToManyField(Student,null=True)
    facultyPublication=models.ManyToManyField(Faculty)
    def __str__(self):
        return self.title