from django.urls import path
from .views import AllBlogView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView,post_list_admin,AddCommentView

app_name = 'blog'

urlpatterns = [
    path('', AllBlogView.as_view(), name='all-blog'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(), name='add-post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('admin_page/', post_list_admin, name="post_list"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),


    
]