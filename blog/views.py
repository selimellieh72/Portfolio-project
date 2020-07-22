from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog
def allblogs(request):
    blogs = blog.objects
    return render(request, "blog/allblogs.html", {"blogs":blogs})
def detailedblog(request,blog_id):
    wholeblog = get_object_or_404(blog, pk=blog_id)
    return render(request, "blog/detailedblog.html", {'blog' : wholeblog})