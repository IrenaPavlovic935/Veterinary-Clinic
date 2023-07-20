from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic 
from django.views.generic import DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import RegisterUserForm, PasswordChangingForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile, Post
from .forms import ProfilePageForm
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('front:index')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Your Where Logged Out"))
    return redirect('front:index')

def register_user(request):
    if request.method == "POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect ('front:index')
    else:
        form= RegisterUserForm()
        
    return render(request, 'users/register.html', {'form': form})

class UserEditView(generic.UpdateView):
    form_class=UserChangeForm
    template_name='users/edit_profile.html'
    success_url= reverse_lazy('front:index')
    
    def get_object(self):
        return self.request.user 

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('users:password_success')
    #form_class = PasswordChangeForm

    
def password_success(request):
    return render(request, 'users/password_success.html')
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'users/create_user_profile_page.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#from django.db.models import Sum

class ShowProfilePageView(DetailView):
    model = Profile
    template_name= 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        context['profile_picture'] = page_user.profile_pic
       

    # Paginacija
        post_list = Post.objects.filter(author__profile=page_user)
        paginator = Paginator(post_list, 3)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts

        if len(posts) > 0:
            context['post'] = posts[0]
        else:
            context['post'] = None


    # Prikazivanje ukupnog broja lajkova za korisničke postove
        user_posts = Post.objects.filter(author=page_user.user)
        total_likes = 0
        for post in user_posts:
            total_likes += post.likes.count()
        context['total_likes'] = total_likes
        
        # Prikazivanje ukupnog broja komentara za korisničke postove
        user_posts = Post.objects.filter(author=page_user.user)
        total_comments = 0
        for post in user_posts:
            total_comments += post.comments.count()
        context['total_comments'] = total_comments
    
        return context
    

from django.urls import reverse_lazy
from django.views import generic
from blog.models import Profile

class EditProfilePageView( generic.UpdateView):
    model = Profile
    template_name = 'users/edit_profile_page.html'
    fields = ['biography', 'profile_pic', 'instagram_url', 'phone', 'email', 'birthday']
    success_url = reverse_lazy('front:index')

    """ def test_func(self): # provjerava da li user mozde urediti taj profil odnosno je li njegov 
        profile = self.get_object()
        return self.request.user == profile.user"""
    
    

def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('front:index')
    return render(request, 'users/delete_profile.html')


