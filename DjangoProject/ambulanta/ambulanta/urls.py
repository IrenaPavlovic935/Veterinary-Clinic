"""ambulanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from blog.admin import blog_site

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/',blog_site.urls),
    
    path('', include('front.urls', namespace='front')),
    #path('front/', include('front.urls', namespace='front')),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('post/', include ('club.urls', namespace='post')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('appointment/', include ('appointment.urls', namespace='appointment')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.index_title="Paws Care"
admin.site.site_header="Paws Care Admin"
admin.site.site_title= "Paws Care"