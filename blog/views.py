from django.shortcuts import render , get_object_or_404
from .models import BlogConfig

def allblogs(request):
    blogs = BlogConfig.objects
    return render(request,'blog/allblogs.html',{'blogs': blogs})

def detail(request , blog_id ):
    detailblog = get_object_or_404(BlogConfig , pk=blog_id)
    return render(request , 'blog/detail.html',{'blog':detailblog})
