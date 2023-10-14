# Create a new Django project
django-admin startproject attendance_project

# Navigate to the project directory
cd attendance_project

# Create a new Django app
python manage.py startapp attendance_app

# In the "models.py" file within the "attendance_app" app, define your models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()
