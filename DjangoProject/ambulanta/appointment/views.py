from django.shortcuts import render, redirect
from .models import Patient, Appointment
from datetime import datetime
from .forms import PatientForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from django.utils.timezone import make_aware

def appointment(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    patient_form = PatientForm()

    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        
        if patient_form.is_valid():
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')
            animal_species = request.POST.get('animal_species')
            animal_breed = request.POST.get('animal_breed')
            appointment_reason = request.POST.get('appointment_reason')
            email = request.POST.get("email")
            animal_age=request.POST.get("animal_age")
            appointment_datetime = datetime.strptime(appointment_date + ' ' + appointment_time, '%Y-%m-%d %H:%M')
            appointment_datetime = make_aware(appointment_datetime)  
            end_datetime = appointment_datetime + timedelta(hours=1)


            
            existing_appointments = Appointment.objects.filter(
                appointment_datetime__gte=appointment_datetime - timedelta(hours=1),
                appointment_datetime__lte=end_datetime + timedelta(hours=1)
            )
            if existing_appointments.exists():
                return render(request, 'appointment/appointment.html',
                              {'message': 'On date and time is already booked. Please choose another date and time.'})

            if appointment_datetime.weekday() == 6:
                return render(request, 'appointment/appointment.html',
                              {'message': 'Scheduling on sundays is not possible'})

            if appointment_datetime.hour < 8 or appointment_datetime.hour >= 18:
                return render(request, 'appointment/appointment.html',
                              {'message': 'You can schedule appointments only between 8 AM and 6 PM'})

            patient_name = patient_form.cleaned_data['patient_name']
            patient, created = Patient.objects.get_or_create(user=request.user)
            patient.patient_name = patient_name
            patient.save()

            appointment = Appointment(patient=patient, appointment_datetime=appointment_datetime,
                                      appointment_reason=appointment_reason,
                                      animal_species=animal_species, animal_breed=animal_breed, email=email, animal_age=animal_age)
            appointment.save()
            username = request.user.username

            subject = 'New Scheduled Appointment'
            context = {
                'patient_name': patient.patient_name,
                'appointment_datetime': appointment_datetime,
                'username':username
            }
            message = render_to_string('appointment/new_appointment.html', context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_DOCTOR, email]

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                html_message=message
            )

            return render(request, 'appointment/appointment.html',
                          {'message': 'Appointment successfully scheduled!'})

    return render(request, 'appointment/appointment.html', {'patient_form': patient_form})





from django.core.paginator import Paginator

def appointment_list(request):
    if not request.user.is_authenticated:
        message = 'You must be logged in to view the list of appointments.'
        return render(request, 'appointment/appointment_list.html', {'message': message})

    
    appointments = Appointment.objects.filter(patient__user=request.user)
    

    paginator = Paginator(appointments, 3) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if page_obj.has_previous():
        previous_page_number = page_obj.previous_page_number()
    else:
        previous_page_number = None

    if page_obj.has_next():
        next_page_number = page_obj.next_page_number()
    else:
        next_page_number = None

    context = {
        'appointments': page_obj,
        'previous_page_number': previous_page_number,
        'next_page_number': next_page_number,
    }
    
    if appointments.exists():
        return render(request, 'appointment/appointment_list.html', context)
    else:
        is_patient = hasattr(request.user, 'patient') #provjeravamo da li request.user objekt ima atribut patient
        context['is_patient'] = is_patient
        return render(request, 'appointment/appointment_list.html', context)



def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if appointment.patient.user != request.user:
        return HttpResponse("Nemate ovlaštenje za otkazivanje ovog termina.")

    if request.method == 'POST':
        # Logika za otkazivanje termina
        appointment.delete()

        # Slanje email poruke o otkazivanju
        subject = 'Your scheduled appointment has been canceled'
        context = {
            'patient_name': appointment.patient.patient_name,
            'appointment_datetime': appointment.appointment_datetime
        }
        message = render_to_string('appointment/send_cancle.html', context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_DOCTOR, appointment.email]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            html_message=message
        )

        return redirect('appointment:appointment_list')
    return render(request, 'appointment/update_appointment.html', {'appointment': appointment})





def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if appointment.patient.user != request.user:
        return HttpResponse("Nemate ovlaštenje za ažuriranje ovog termina.")

    if request.method == 'POST':
        appointment.patient.patient_name = request.POST.get('patient_name')
        appointment.animal_species = request.POST.get('animal_species')
        appointment.animal_breed = request.POST.get('animal_breed')
        appointment.animal_age = request.POST.get('animal_age')
        appointment.appointment_datetime = request.POST.get('appointment_date') + ' ' + request.POST.get('appointment_time')
        appointment.appointment_reason = request.POST.get('appointment_reason')
        appointment.email = request.POST.get('email')

        new_appointment_datetime = datetime.strptime(appointment.appointment_datetime, '%Y-%m-%d %H:%M')

        if new_appointment_datetime.weekday() == 6:
            return render(request, 'appointment/update_appointment.html',
                          {'appointment': appointment, 'message': 'Scheduling on sundays is not possible'})

        if new_appointment_datetime.hour < 8 or new_appointment_datetime.hour >= 18:
            return render(request, 'appointment/update_appointment.html',
                          {'appointment': appointment, 'message':  'You can schedule appointments only between 8 AM and 6 PM'})

        appointment.save()
        subject = 'Your scheduled appointment has been rescheduled for'
        context = {
            'patient_name': appointment.patient.patient_name,
            'appointment_datetime': appointment.appointment_datetime
        }
        message = render_to_string('appointment/send_update.html', context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_DOCTOR, appointment.email]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            html_message=message
        )

        return redirect('appointment:appointment_list')

    return render(request, 'appointment/update_appointment.html', {'appointment': appointment})














"""               
            subject = 'Novi zakazani termin'
            message = f'Pacijent: {patient.patient_name}, Datum i vrijeme: {appointment_datetime}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = settings.EMAIL_HOST_DOCTOR

            send_mail(subject, message, from_email,[recipient_list, Appointment.email ])
            #email.send()
            U Django ORM-u, __gte i __lte su specifični operatori koji se koriste za usporedbu u upitima kako bi se filtrirali objekti na temelju vrijednosti polja.
"""  





    
"""
doctor_email = 'irena.p.1409003@gmail.com'  
subject = 'Novi zakazani termin'
message = f'Pacijent: {patient.patient_name}, Datum i vrijeme: {appointment_datetime}'
from_email = settings.EMAIL_HOST_USER
recipient_list = [doctor_email]
send_mail(subject, message, from_email, recipient_list)
"""