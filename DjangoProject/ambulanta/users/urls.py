from django.urls import path
from .views import UserEditView,login_user,logout_user,register_user,PasswordsChangeView,ShowProfilePageView,EditProfilePageView, CreateProfilePageView,delete_profile
from django.contrib.auth import views as auth_views
from . import views
app_name = 'users'



urlpatterns = [
    path('login_user', login_user,name="login"),
    path('logout_user', logout_user, name='logout'),
    path('register_user', register_user, name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/',PasswordsChangeView.as_view(template_name='users/change_password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
    #path('<str:user>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_user_profile_page/', CreateProfilePageView.as_view(), name="create_user_profile_page"),
    path('profile/delete/',delete_profile, name='delete_profile'),
    
   


    
    
]