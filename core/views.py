from django.http import HttpResponse
from django.shortcuts import render
from core.models import Blog, Category,Contact, Setting,Product,FAQ
from core.forms import ContactUsForm
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from excel_response import ExcelResponse,ExcelView
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact.html',context={'contact_form':ContactUsForm})
        else:
            print('Form errors:  ', form.errors)
    context={
        'contact_form':ContactUsForm,
        'contacts':Contact.objects.filter(is_active=True),
        'title':'Contact Page',
    }
    return render(request,'contact.html',context)
def blog(request):
    user_input=None
    start_date=None
    end_date=None
    
    category=Category.objects.filter(is_active=True)
    blogs=Blog.objects.filter(is_active=True)

   
 
    if request.method=='POST':
        user_input=request.POST.get('blog_search')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        category=request.POST.get('category')
        print('cat@@', category)
        if category:
            blogs=blogs.filter(category__id=category)
            print('blog@@', blogs)
        if user_input:
            blogs=blogs.filter(title__icontains=user_input)
        if start_date and end_date:
            blogs=blogs.filter(
                Q(created_at__date__gte=start_date)&
                Q(created_at__date__lte=end_date)
            )
        context={
            'categories':Category.objects.filter(is_active=True),
            'blogs':blogs,
            'blog_count':len(blogs) ,
            'no_result':'blog tapilmadi' if not blogs else None,

        }
        return render(request, 'blog.html', context=context)
    items_per_page=2
    paginator=Paginator(blogs,items_per_page)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)

    context={
        'blogs':blogs,
        'title':Setting.objects.get(id=1),
        'blog_count':len(blogs) ,
        'no_result':'blog tapilmadi' if not blogs else None,
        'user_input':user_input,
        'start_date':start_date,
        'end_date':end_date,
        'categories':category,

    }
   

    return render(request,'blog.html',context=context)

        
        
    
def blogdetails(request,blog_slug):
    blog=Blog.objects.get(slug=blog_slug)
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
    products=Product.objects.filter(is_active=True)
    context={
        'categories':products,
        'title':'Category'
    }
    return render(request,'category.html' ,context=context )
def singleproduct(request):
    return render(request,'single-product.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')


# def faq(request):
#     context={
#         'faqs':FAQ.objects.filter(is_active=True),
#     }
#     return render(request,'faq.html',context=context)


class  FAQView(ListView):
    # model=FAQ
    template_name='faq.html'
    context_object_name='faqs'
    queryset=FAQ.objects.filter(is_active=True)


def all_search(request):
    blogs=Blog.objects.filter(is_active=True)
    products=Product.objects.filter(is_active=True)
    if request.method=='POST':
        user_input=request.POST.get('all-search')
        blogs=Blog.objects.filter(title__icontains=user_input)
        products=Product.objects.filter(name__icontains=user_input)
       

    context={
        'title':'search',
        'blogs':blogs ,
        'categories':products ,
        
         }

    return render(request,'search.html',context)

# def export_blogs_excel(request):
#     blogs = Blog.objects.filter(is_active=True)
#     response = ExcelResponse()
#     worksheet = response.workbook.add_worksheet()
#     worksheet.write(0, 0, 'ID')
#     worksheet.write(0, 1, 'Title')
#     worksheet.write(0, 2, 'Category')
#     worksheet.write(0, 3, 'Date')
#     row = 1
#     for blog in blogs:
#         worksheet.write(row, 0, blog.id)
#         worksheet
    

# def export_blogs_excel(request):
#     response=ExcelResponse(Blog.objects.filter(is_active=True),output_filename='blogs')
#     # response['Content-Disposition']='attachment; filename=blogs.xlsx' 
#     return response


def export_blogs_excel(request):
    objs = Blog.objects.filter(is_active=True).values('id','title','category__name','created_at')
    return ExcelResponse(objs)

# class ModelExportView(ExcelView):
#     model = Blog


def error_404(request, exception):
    return render(request, '404.html', status=404)



