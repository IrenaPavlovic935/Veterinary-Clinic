from django.shortcuts import render, redirect, reverse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# import Pagination Stuff
from django.core.paginator import Paginator


#def all_events(request):
    #event_list= Event.objects.all()
    #return render(request, 'club/club.html', {'event_list' : event_list})
# Create your views here.

def all_events(request):
    event_list = Event.objects.all().order_by('name')
    context = { "event_list" : event_list }
    return render(request, 'club/club.html', context)

def add_venue(request):
    submitted=False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('post:add-venue') + '?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'club/add_venue.html',{"form": form, "submitted": submitted})

def list_venues(request):
    venue_list = Venue.objects.all()
    p = Paginator(Venue.objects.all(), 2)
    page= request.GET.get('page')
    venues = p.get_page(page)
    
    return render(request, 'club/venue.html',
                  { "venue_list" : venue_list ,
                   'venues' : venues}
                )


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'club/show_venue.html',
                  {'venue': venue})
from blog.models import Post,Profile
"""def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        
        venues = Venue.objects.filter(name__contains=searched)
        posts = Post.objects.filter(title__contains=searched)
        profiles = Profile.objects.filter(user__username__icontains=searched)
        
        return render(request, 'club/search.html', {'searched': searched, 'venues': venues, 'posts': posts, 'profiles': profiles})
    else:
        return render(request, 'club/search.html')
def mobile_search(request):
    if request.method == "POST":
        searchedd = request.POST['searchedd']
        print(searchedd) 
        
        venues = Venue.objects.filter(name__contains=searchedd)
        posts = Post.objects.filter(title__contains=searchedd)
        profiles = Profile.objects.filter(user__username__icontains=searchedd)
        
        return render(request, 'club/search_mobile.html', {'searchedd': searchedd, 'venues': venues, 'posts': posts, 'profiles': profiles})
    else:
        return render(request, 'club/search_mobile.html')"""
    
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('club:list-venues')
    return render(request, 'club/update_venue.html',
                  {'venue': venue, 'form': form})
    
def add_event(request):
    submitted=False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('post:add-event') + '?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'club/add_event.html',{"form": form, "submitted": submitted})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    #print(event, "OVO JE KEY")
    if form.is_valid():
         form.save()
         return redirect('club:club')
    return render(request, 'club/update_event.html',
                  {'event': event,'form': form})
    
#delete an event 
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('club:club')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('club:list-venues')

# Generate Text File Venue List
def venue_text(request):
    resposne=HttpResponse(content_type='text/plain')
    resposne['Content-Disposition'] = 'attachment; filname=venues.txt'
    venues= Venue.objects.all()
    # Creat e blank list
    lines= []
    # loop thu and output
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n\n\n\n')
    
    #lines= ["This is line 1\n",
    #        "This is line 2\n",
    #        "This isline 3\n"]
    
    #Write to textfile
    resposne.writelines(lines)
    return resposne