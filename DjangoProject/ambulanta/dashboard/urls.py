from django.urls import path
from .views import   add_image, gallery,delete_image, detail_image,add_comment,like_comment, add_reply, delete_comment, delete_reply,like_reply,search_venues,mobile_search

app_name = 'dashboard'

urlpatterns = [
    #path('', dashboard, name='dashboard'),
    path('add_image/', add_image, name='add-image'),
    path('gallery/', gallery, name='gallery'),
    path('dashboard/gallery/delete/<int:image_id>/', delete_image, name='delete_image'),
    path('gallery/<int:image_id>/', detail_image, name='detail_image'),
    path('image/<int:image_id>/add_comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/like/', like_comment, name='like_comment'),
    path('reply/<int:reply_id>/like/', like_reply, name='like_reply'),
    path('add_reply/<int:comment_id>/', add_reply, name='add_reply'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('delete_reply/<int:reply_id>/', delete_reply, name='delete_reply'),
    path('search_venues', search_venues, name='search-venues'),
    path('mobile_search/',mobile_search, name='mobile-search'),

]
  

    
   





