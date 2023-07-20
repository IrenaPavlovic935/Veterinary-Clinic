from django.shortcuts import render
#from .models import Page
from django.shortcuts import render, redirect
from django.views.generic import  CreateView
from .models import GalleryImage
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm
"""def dashboard(request):
    context = {'page_obj': Page.objects.all().first()}
    return render(request, 'front/index.html', context)

def get_context_data(self, *args, **kwargs):
    context = super(dashboard, self).get_context_data(*args, **kwargs)
    context['page_obj'] = Page.objects.all().first()
    return context
"""
# Create your views here



from django.shortcuts import render, redirect
from .forms import GalleryImageForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import GalleryImageForm

def add_image(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = GalleryImageForm(request.POST, request.FILES)
            if form.is_valid():
                gallery_image = form.save(commit=False)
                gallery_image.user = request.user
                gallery_image.save()

                # Dobi URL slike
                image_url = gallery_image.image.url

                # Čuvaj URL slike u bazi podataka
                gallery_image.url = image_url
                gallery_image.save()

                return redirect('front:index')
            else:
                messages.error(request, "There was an error processing the form.")
        else:
            messages.info(request, "You must be logged in to add an image.")
            form = GalleryImageForm()
    else:
        form = GalleryImageForm()

    context = {'form': form}
    return render(request, 'dashboard/upload_image.html', context)

"""
def gallery(request):
    gallery_images = GalleryImage.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, 'dashboard/gallery.html', context)
"""
def gallery(request):
    gallery_images = GalleryImage.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, 'dashboard/gallery.html', context)

from django.shortcuts import get_object_or_404, redirect

def delete_image(request, image_id):
    gallery_image = get_object_or_404(GalleryImage, id=image_id, user=request.user)

    if request.method == 'POST':
       
        if gallery_image.user != request.user:
            return redirect('front:gallery')
        else:
            gallery_image.delete()
        return redirect('dashboard:gallery')


    context = {'gallery_image': gallery_image}
    return render(request, 'dashboard/delete_image.html', context)


"""
def LikeGalleryView(request, pk):
    gallery_id =  request.POST.get('gallery_id')
    if gallery_id:
        post = get_object_or_404(GalleryImage, id=gallery_id)
        post.likes.add(request.user)
    return redirect('dashboard:gallery')

def LikeGalleryView(request):
    post=get_object_or_404(GalleryImage, id= request.POST.get('gallery_id'))
    post.likes.add(request.user)
    return redirect('dashboard:gallery')
"""

"""
def detail_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    is_liked = image.likes.filter(id=request.user.id).exists()

    if request.method == 'POST':
        if is_liked:
            image.likes.remove(request.user)
        else:
            image.likes.add(request.user)
        return redirect('dashboard:detail_image', image_id=image_id)

    context = {'image': image, 'is_liked': is_liked}
    return render(request, 'dashboard/detail_image.html', context)
"""
def detail_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    is_liked = image.likes.filter(id=request.user.id).exists()
    comments = image.comments.all()

    if request.method == 'POST':
        if is_liked:
            image.likes.remove(request.user)
        else:
            image.likes.add(request.user)
        return redirect('dashboard:detail_image', image_id=image_id)
    
    total_comments = CommentGallery.objects.filter(post=image).count()
    total_replies = Reply.objects.filter(comment__post=image).count()
    total_comments_and_replies = total_comments + total_replies
    context = {
        'image': image,
        'is_liked': is_liked,
        'comments': comments,
        'total_comments_and_replies': total_comments_and_replies,
    }
    return render(request, 'dashboard/detail_image.html', context)





from django.contrib import messages

from .models import CommentGallery, Reply

from django.db.models import Count

def add_comment(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = image
            comment.user = request.user
            comment.image_id = image_id 
            comment.save()
            return redirect('dashboard:detail_image', image_id=image_id)
    else:
        form = CommentForm()


    context = {
        'image': image,
        'form': form,
      
    }

    return render(request, 'dashboard/add_comment_gallery.html', context)




from .models import CommentGallery
def like_comment(request, comment_id):
    comment = get_object_or_404(CommentGallery, id=comment_id)
    
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    
    return redirect('dashboard:detail_image', image_id=comment.post.id)



from .models import CommentGallery, Reply
from .forms import ReplyForm
def like_reply(request, reply_id):
    reply=get_object_or_404(Reply, id=reply_id)
    if request.user in reply.likes.all():
        reply.likes.remove(request.user)
    else:
        reply.likes.add(request.user)
    return redirect('dashboard:detail_image', image_id=reply.comment.post.id)


def add_reply(request, comment_id):
    comment = get_object_or_404(CommentGallery, id=comment_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user
            reply.parent_reply_id = request.POST.get('parent_reply_id')  
            reply.save()
            return redirect('dashboard:detail_image', image_id=comment.post.id)
    else:
        form = ReplyForm()

    replies = comment.replies.all()

    """ reply_forms = []
    for reply in replies:
        reply_form = ReplyForm()
        reply_forms.append((reply, reply_form))"""

    context = {
        'comment': comment,
        'form': form,
        'replies': replies,
        #'reply_forms': reply_forms,
    }

    return render(request, 'dashboard/add_reply.html', context)



from django.contrib import messages

def delete_comment(request, comment_id):
    comment = get_object_or_404(CommentGallery, id=comment_id)

    if comment.user == request.user or request.user.is_superuser:
        comment.delete()
        messages.success(request, "The comment has been successfully deleted.")
    else:
        messages.error(request, "You do not have permission to delete this comment.")

    return redirect('dashboard:detail_image', image_id=comment.post.id)


from django.contrib import messages

def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)

    # Provjerite da li trenutni korisnik ima ovlaštenje za brisanje odgovora
    if reply.user == request.user:
        reply.delete()
        messages.success(request, "The reply has been successfully deleted.")
    else:
        messages.error(request, "You do not have permission to delete this reply.")

    return redirect('dashboard:detail_image', image_id=reply.comment.post.id)

from blog.models import Post,Profile
def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        
        
        posts = Post.objects.filter(title__icontains=searched)
        profiles = Profile.objects.filter(user__username__icontains=searched)
        
        return render(request, 'dashboard/search.html', {'searched': searched,  'posts': posts, 'profiles': profiles})
    else:
        return render(request, 'dashboard/search.html')
def mobile_search(request):
    if request.method == "POST":
        searchedd = request.POST['searchedd']
        
       
        posts = Post.objects.filter(title__contains=searchedd)
        profiles = Profile.objects.filter(user__username__icontains=searchedd)
        
        return render(request, 'dashboard/search_mobile.html', {'searchedd': searchedd,  'posts': posts, 'profiles': profiles})
    else:
        return render(request, 'dashboard/search_mobile.html')
