from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=20)
    phone = models.IntegerField(max_length=10)
    location = models.TextField()

    def __str__(self):
        return self.name

class Patients(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=20)
    phone = models.IntegerField(max_length=10)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE) #eliminar los valores en caso de borrar a algun doctor
    consult = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.doctor.name