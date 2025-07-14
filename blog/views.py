from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.filter(is_published=True)
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(is_published=True).exclude(id=blog_post.id)[:3]
    
    context = {
        'blog_post': blog_post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)
