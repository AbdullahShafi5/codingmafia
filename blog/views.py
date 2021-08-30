from django.shortcuts import render,HttpResponse
from blog.models import Posts
from django.core.paginator import Paginator
import math
def blogHome(request):
    # allposts = Posts.objects.all()
    # context = {'allposts':allposts}
    # return render(request,'blog/blogHome.html' , context)no_of_posts = 3
    no_of_posts = 3
    pages = request.GET.get('page')
    if pages is None:
        pages = 1 
    else:
        pages = int(pages) 

    allposts = Posts.objects.all()
    length = len(allposts)
    allposts= allposts[(pages-1)*no_of_posts: pages*no_of_posts]
    if pages>1:
        prev = pages - 1
    else:
        prev = None
    if pages < math.ceil(length/no_of_posts):
        nxt  = pages + 1
    else:
        nxt = None
    context = {'allposts':allposts , 'prev':prev ,'nxt':nxt }
    return render(request,'blog/blogHome.html' , context)


def blogPost(request,slug):
    post = Posts.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request,'blog/blogPost.html', context)

