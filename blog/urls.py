from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<int:blog_post_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog_post, name='add_blog'),
    path('edit/<int:blog_post_id>/', views.edit_blog, name='edit_blog'),
    path(
         'delete/<int:blog_post_id>/',
         views.delete_blog_post,
         name='delete_blog_post'),
    path(
         'comment/delete/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
]
