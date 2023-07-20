from django.urls import path
from . import views
from django.urls import path
from .views import AllSentMessagesView

app_name = 'front'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/thankyou/', views.thankyou, name='thankyou'),
    path('messages/sent/', AllSentMessagesView.as_view(), name='all_sent_messages'),
]