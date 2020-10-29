from django.shortcuts import render
from blogs.models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
# Create your views here.

def blogs_home(request):
    blogs_list = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs_list, 8)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request,'blog-two-column.html',{'blogs':blogs})

def blog_single(request, slug):
    object = get_object_or_404(Blog, slug = slug)
    return render(request,'blog-details-right-sidebar.html',{'blog':object})

