from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)



    """@property
    def is_waiting(self):
        return bool(self.waiting_status) # pitati za ovo"""


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    animal_species=models.CharField(max_length=100)
    animal_breed=models.CharField(max_length=100)
    appointment_reason = models.TextField()
    appointment_datetime = models.DateTimeField()
    email = models.CharField(max_length=254, blank=False)
    animal_age=models.IntegerField(max_length=100, null=True)
    
    """    def __str__(self):
        return f"{self.patient.patient_name} - {self.appointment_datetime}"""

