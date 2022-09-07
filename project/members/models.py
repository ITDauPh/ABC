from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.TextField()
    def __str__(self):
        return self.first_name
        
# Create your models here.
