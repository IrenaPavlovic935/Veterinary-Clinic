from typing import Any, Dict
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from.forms import PostFrom, EditFrom,CommentForm
from django.db.models import Sum
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.db.models import Count
from.models import Profile, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

class AllBlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by= 4
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments_count = post.comments.count()
        context['comments_count'] = comments_count
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        
        return context
class AddPostView(CreateView):
    model = Post
    form_class= PostFrom
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    
class UpdatePostView(UpdateView):
    model= Post
    form_class=EditFrom
    template_name= 'blog/update_post.html'
    #fields = ['title', 'title_tag', 'body']
    
class DeletePostView(DeleteView):
    model= Post
    template_name= 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all-blog')
    
def LikeView(request, pk):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('blog:article-detail', args=[str(pk)]))
    
def post_list_admin(request):
    blog_list = Post.objects.all()
    paginator = Paginator(blog_list, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'blog_list':blog_list
    }
    return render(request, 'blog/blog_admin.html', context)



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
    """
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'user': self.request.user}
        return kwargs"""
    """   def comment_count(self):
        return self.comments.count()"""

    success_url = reverse_lazy('blog:all-blog')