from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, BlogPost, UserProfile
from .forms import CommentForm  # Import the CommentForm if you haven't already
from django.contrib.auth.decorators import login_required

def index(request):
    data = BlogPost.objects.filter(status='published').order_by('-published_at')
    return render(request, 'index.html', {'blogs_data': data})

def blog_page(request, blog_title):
    blog_post = get_object_or_404(BlogPost, title=blog_title, status='published')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_post
            comment.author = request.user  # Assuming you have user authentication
            comment.save()
            form = CommentForm()  # Clear the form after submission
    else:
        form = CommentForm()
    
    comments = Comment.objects.filter(post=blog_post)
    
    return render(request, 'blog_page.html', {'blog_data': blog_post, 'comments': comments, 'form': form})

@login_required  # Requires user authentication
def add_comment(request, blog_title):
    blog_post = get_object_or_404(BlogPost, title=blog_title, status='published')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_post
            comment.author = request.user  # Assuming you have user authentication
            comment.save()
            form = CommentForm()  # Clear the form after submission
            return redirect('blog_page', blog_title=blog_title)  # Redirect back to the blog page after submission
    else:
        form = CommentForm()
    
    return render(request, 'blog_page.html', {'blog_data': blog_post, 'form': form})
