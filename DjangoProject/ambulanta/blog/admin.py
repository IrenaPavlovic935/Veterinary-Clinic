from django.contrib import admin
from .models import Post,Profile, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)



class BlogAdminArea(admin.AdminSite):
   site_header = 'Blog Admin Area'

blog_site = BlogAdminArea(name='BlogAdmin')
blog_site.register(Post)
    

