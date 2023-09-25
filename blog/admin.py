from django.contrib import admin
from .models import Comment,BlogPost,UserProfile

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('author','post','created_at',)
    list_filter=('author','post','created_at',)
    search_fields=('author','post','created_at',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','author','published_at','status',)
    list_filter=('author','published_at','status','updated_at',)
    search_fields=('title','author','published_at','status','updated_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('get_profile_picture','user',)
    readonly_fields=('get_profile_picture',)
# admin.site.register(UserProfile)