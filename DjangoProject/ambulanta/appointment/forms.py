
from django import forms
from .models import Patient
from .models import Appointment

class PatientForm(forms.ModelForm):
    patient_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    animal_age = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'age'})) 
  

    class Meta:
        model = Patient
        fields = ['patient_name', 'appointment_date', 'appointment_time', 'animal_age']


