from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

num = [1,2,3,4,5,6,7,8,9]

def blog(request):
    ints = {
        'nums' : num
    }
    return render( request , 'blog/blog.html', ints )

def blog_about(request):
    return render(request, 'blog/blog-about.html')

