from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""class Page(models.Model):
    title = models.CharField(max_length=200)
    title_description= models.TextField(blank=True, null=True)
    body=models.TextField(blank=True, null=True)
    content =models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title"""
    


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='gallery_posts')

    def __str__(self):
        return str(self.id)
    
class CommentGallery(models.Model):
    post = models.ForeignKey(GalleryImage, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments')
 



    def __str__(self):
        return str(self.id)

class Reply(models.Model):
    comment = models.ForeignKey(CommentGallery, related_name='replies', on_delete=models.CASCADE)
    parent_reply = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_reply')
    replied_to = models.ForeignKey('self', null=True, blank=True, related_name='replies_received', on_delete=models.CASCADE)


    
    