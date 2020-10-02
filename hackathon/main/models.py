from django.db import models
from gdstorage.storage import GoogleDriveStorage
#nL5l95DThPKoqRer8lfnwmZd
#338840529605-dlpeu4tajelf6otrnkuj0852r0ce3ag9.apps.googleusercontent.com
# Create your models here.
gd_storage = GoogleDriveStorage()


class department(models.Model):
    department_id=models.CharField(max_length=10)

class teacher(models.Model):
    teacher_id=models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    mailid=models.EmailField()
    password=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    department_id=models.ManyToManyField(department)



class student(models.Model):
    full_name=models.CharField(max_length=100)
    mailid=models.EmailField()
    password=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    department_id=models.ManyToManyField(department)
    student_id = models.CharField(max_length=100)



class courses(models.Model):
    course_name= models.CharField(max_length=100)
    course_id=models.CharField(max_length=100)
    department_id=models.ManyToManyField(department)



class studentcourse(models.Model):
    course_id=models.ManyToManyField(courses)
    student_id= models.ManyToManyField(student)



class teachercourse(models.Model):
    course_id=models.ManyToManyField(courses)
    teacher_id=models.ManyToManyField(teacher)
    
        
class file(models.Model):
    map_name = models.CharField(max_length=200)
    map_data=models.FileField(upload_to='maps',storage=gd_storage)
    course_id=models.ManyToManyField(courses)

    


    
#course ki course register ki relation

#course inka faculty

#files upload modal #file model should have dateofupload and name




