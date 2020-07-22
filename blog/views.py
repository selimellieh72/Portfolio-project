from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog
from .models import tag
def allblogs(request):
	blogs = blog.objects
	return render(request, "blog/allblogs.html", {"blogs":blogs})
def detailedblog(request,blog_id):
    wholeblog = get_object_or_404(blog, pk=blog_id)
    return render(request, "blog/detailedblog.html", {'blog' : wholeblog})
def detailedcategory(request, category_name):
	specific_category = None
	try:
		specific_category = tag.objects.get(tag = category_name)
	except:
		return HttpResponse("No category with the name '{}'".format(category_name))
	if specific_category != None:
		blogs = blog.objects.filter(tag = specific_category)
		return render(request, 'blog/category.html', {'category':specific_category,'blogs':blogs})