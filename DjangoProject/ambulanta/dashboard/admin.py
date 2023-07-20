from django.contrib import admin

# Register your models here.
from .models import  GalleryImage,CommentGallery, Reply

#admin.site.register(Page)
admin.site.register(GalleryImage)
admin.site.register(CommentGallery)
admin.site.register(Reply)