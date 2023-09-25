from django.shortcuts import render
from .models import Comment,BlogPost,UserProfile
# Create your views here.

def index(request):
    data=BlogPost.objects.filter(status='published').order_by('-published_at')
    return render(request,'index.html',{'blogs_data':data})
    # return render(request,'index.html')

def blog_page(request,blog_title):
    data=BlogPost.objects.get(title=blog_title)
    print(data)
    return render(request,'blog_page.html',{'blog_data':data})