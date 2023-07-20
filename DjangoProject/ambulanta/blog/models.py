from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.http import request


class Post(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to= "images/" )
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    """def __str__(self):
        return self.title + ' | ' + str(self.author)"""
    def total_likes(self):
        return self.likes.count()
    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[str(self.id)])



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    biography = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    birthday=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('front:index')

    """ def posts_today(self):
        today = date.today()
        return self.user.post_set.filter(post_date__date=today).count()"""

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)