from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard.models import GalleryImage

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from dashboard.models import Page
"""
def index(request):
    context = {
        'page_obj': Page.objects.first()
    }
    return render(request, 'front/index.html', context)
"""
from django.shortcuts import render
from dashboard.models import GalleryImage

def index(request):
    gallery_images = GalleryImage.objects.order_by('-date_published')[:6]

    context = {
        #'page_obj': Page.objects.first(),
        'gallery_images': gallery_images
    }
    return render(request, 'front/index.html', context)

"""def contact(request):
    return render(request, 'front/contact.html')

from django.shortcuts import render
"""
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Message



def thankyou(request):
    submission_message = None

    if request.method == 'POST':

        message_content = request.POST.get('message')
        recipient = request.user
        message = Message.objects.create(sender=request.user, recipient=recipient, content=message_content)
        message.save()

        submission_message = "Thank you for your message!"  

    return render(request, 'front/contact.html', {'submission_message': submission_message})


from django.views.generic import ListView
from .models import Message

class AllSentMessagesView(ListView):
    model = Message
    template_name = 'users/all_sent_messages.html'
    context_object_name = 'messages'

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user)