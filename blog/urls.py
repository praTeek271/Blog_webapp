from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog_page/<str:blog_title>',views.blog_page,name='blog_page'),
    path('blog_page/<str:blog_title>/add-comment/', views.add_comment, name='add_comment'),
]