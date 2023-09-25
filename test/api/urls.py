# api/urls.py
from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView, CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('blog/', BlogPostListCreateView.as_view(), name='blogpost'),
    path('blog/<int:pk>', BlogPostRetrieveUpdateDestroyView.as_view(), name='blogpost-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]
