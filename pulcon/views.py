from django.shortcuts import render
from postdisplay.models import postview

def homepage(request):
    postData = postview.objects.all()
    if request.method =="GET":
        st = request.GET.get('postname')
        if st != None:
            postData = postview.objects.filter(post_title__icontains=st)
    data = {
        'postData': postData
    }
    return render(request,"index.html",data)

def createpost(request):
    return render(request, "createpost.html")

def lostandfound(request):
    return render(request, "lostandfound.html")

def studygroup(request):
    return render(request, "studygroup.html")

def savepost(request):
    if request.method=="POST":
        pt = request.POST.get('postTitle')
        pd = request.POST.get('postDetails')
        pu = request.POST.get('username')
        post = postview(post_title=pt,post_details=pd,post_user=pu)
        post.save()
    return render(request, "index.html")

def postDetails(request,slug):
    postdetails = postview.objects.get(slug=slug)
    data={
        'postdetails': postdetails
    }
    return render(request,"postdetails.html",data)
