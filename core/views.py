from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def blogdetails(request):
    return render(request,'single-blog.html')
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
