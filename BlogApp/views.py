from django.shortcuts import render
from .models import Post,User
# Create your views here.
def IndexView(request):
    
    data = {'posts':Post.objects.all()}
    return render(request,'BlogApp/Index.html',context=data)

def SignUp(request):
    pass

def Login(request):
    pass
