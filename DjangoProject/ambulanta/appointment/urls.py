from django.urls import path
from .views import appointment,appointment_list,cancel_appointment,update_appointment

app_name = 'appointment'

urlpatterns = [
    path('appointment/', appointment, name='appointment'),
    path('list/', appointment_list, name='appointment_list'),
    path('cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('update/<int:appointment_id>/', update_appointment, name='update_appointment')


    
     
    #path('', views.all_events, name="list-events")
    
    #path('test/', views.test, name="test"),
]
