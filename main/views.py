from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial, ContactMessage
from menu.models import MenuItem
from blog.models import BlogPost

def home(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    featured_menu_items = MenuItem.objects.filter(is_featured=True)[:6]
    latest_blog_posts = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'testimonials': testimonials,
        'featured_menu_items': featured_menu_items,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'main/home.html', context)

def about(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'main/about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'main/contact.html')
