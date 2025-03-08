from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
