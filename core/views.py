from django.shortcuts import render
from core.models import Blog,Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    context={
        'contacts':Contact.objects.filter(is_active=True),
        'title':'Contact Page',
    }
    return render(request,'contact.html',context=context)
def blog(request):
    context={
        'blogs':Blog.objects.filter(is_active=True).order_by('-created_at'),
        'title':'Blog Page',
        'blog_count':Blog.objects.filter(is_active=True).count()
    }
    return render(request,'blog.html',context=context)
def blogdetails(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    context={
        'title':blog.title,
        'blog':blog
    }
    return render(request,'single-blog.html',context=context)
def elements(request):
    return render(request,'elements.html')
def tracking(request):
    return render(request,'tracking.html')
def category(request):
    return render(request,'category.html')
def singleproduct(request):
    return render(request,'single-product.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
