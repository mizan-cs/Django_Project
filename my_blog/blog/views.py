from django.shortcuts import render
from blog.models import Post_DB

def blog_home(request):

    posts = Post_DB.objects.all()

    if 'category' in request.GET:
        posts = posts.filter(category=int(request.GET.get('category')))

    ct = {
        'posts':posts.order_by('-date')
    }
    return render(request,'home.html',ct)

def blog_post(request, pk):
    post = Post_DB.objects.get(pk=pk)
    return render(request,'post.html',{'post':post})
