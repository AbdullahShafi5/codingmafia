from django.shortcuts import render,redirect , HttpResponse 
from home import views
from .models import Contact
from django.contrib import messages
from blog.models import Posts
def home(request):
    allposts = Posts.objects.all() 
    context = {'allposts':allposts}
    if request.method =="POST":
        print("it's working")
        sbs_name = request.POST.get('name') 
        print(sbs_name)
    return render(request,"home/home.html",context)

def about(request):
    return render(request,'home/about.html')    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')        
        contact = Contact(name=name , email=email , phone = phone , content = content)
        contact.save()
        messages.success(request , 'Message sent successfuly ')        
    return render(request,'home/contact.html')
    
def search(request):
    query = request.GET['query']
    if len(query) > 30:
        allposts = Posts.objects.none()
    else:
        allposttlt = Posts.objects.filter(title__icontains=query)
        allpostCnt = Posts.objects.filter(content__icontains=query)
        allposts  = allposttlt.union(allpostCnt)
    
    pems = {'allposts':allposts , 'query':query  }
    return render(request  , 'home/search.html', pems)