from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .Codes import *
from .models import Post,User
from django.utils import timezone
from re import search

def IndexView(request):
    isAdmin = False
    isLoggedIn = False
    if request.session.get('email',None) is not None:
            isAdmin = User.objects.get(Email=request.session['email']).IsAdmin
            isLoggedIn = True
    data = {'posts':Post.objects.all().order_by('-Date'),'isAdmin':isAdmin,'isLoggedIn':isLoggedIn}
    return render(request,'BlogApp/Index.html',context=data)

def SignUp(request):
    if request.session.get('email',None) is not None:
        # If Logged In, Redirect
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        if request.POST['password'] == '' or request.POST['repassword'] == '' or request.POST['name'] == '':
            # Email has regex to verify it
            return render(request,'BlogApp/SignUp.html',context = {'error':'All Fields Are Required'})
        if search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",request.POST['email']):
            # Email Validation
            return render(request,'BlogApp/SignUp.html',context = {'error':'Email is Invalid'})
        if User.objects.filter(email=request.POST['email']):
            return render(request,'BlogApp/SignUp.html',context = {'error':'Email is Already Used'})
        if request.POST['password'] != request.POST['repassword']:
            return render(request,'BlogApp/SignUp.html',context = {'error':'Passwords Don\'t match'})
        user = User.objects.create(Email=request.POST['email'],Name=request.POST['Name'],Password=request.POST['password'])
        user.save()
        request.session['email'] = user.Email
        return HttpResponseRedirect('/')
    
    return render(request,'BlogApp/SignUp.html')
def LogIn(request):
    if request.session.get('email',None) is not None:
        # If Logged In, Redirect
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        user = User.objects.filter(Email=request.POST['email'])
        if user:
            if user[0].Password == request.POST['password']:
                request.session['email'] = user[0].Email
                return HttpResponseRedirect('/')
        return render(request,'BlogApp/LogIn.html',context={'error':'Invalid Credentials'})
    return render(request,'BlogApp/LogIn.html')

def like(request):
    # Like/Unlike a Post
    if request.session.get('email',None) is None:
        # User should login to vote
        return
    user = User.objects.get(Email=request.session['email'])
    current_post = Post.objects.get(id=int(request.POST['post_id']))
    if current_post.Votes.filter(Email=request.session['email']):
        # Unlike
        current_post.Likes -= 1
        current_post.Votes.remove(user)
        current_post.save()
        return HttpResponse('-1')
    # Like
    current_post.Likes += 1
    current_post.Votes.add(user)
    current_post.save()
    return HttpResponse('+1')

def edit(request):
    # Edit a post, if admin
    if request.session.get('email',None) is not None:
        if User.objects.get(Email=request.session['email']).IsAdmin:
            try:
                current_post = Post.objects.get(id=int(request.POST['post_id']))
                current_post.content = request.POST['content']
                current_post.save()
                return HttpResponse(SuccessCode)
            except Post.DoesNotExist:
                return HttpResponse(UnknownErrorCode)
    return HttpResponse(UnknownErrorCode)

def delete(request):
    # Delete a post, if admin
    if request.session.get('email',None) is not None:
        if User.objects.get(Email=request.session['email']).IsAdmin:
            try:
                current_post = Post.objects.get(id=int(request.POST['post_id']))
                current_post.delete()
                return HttpResponse(SuccessCode)
            except Post.DoesNotExist:
                return HttpResponse(UnknownErrorCode)
    return HttpResponse(UnknownErrorCode)
            
def get_vote_status(request):
    # Know if user has voted a post
    if request.session.get('email',None) is None:
        return HttpResponse('Like')
    current_post = Post.objects.get(id=request.POST['post_id'])
    if current_post.Votes.filter(Email = request.session['email']):
        return HttpReponse('Liked')
    return HttpResponse('Like')

def newpost(request):
    #
    max_length = 20
    if request.POST['title'] == '' or request.POST['content'] == '':
        return HttpResponse(FaliureCode)
    if len(request.POST['title']) > max_length:
        return HttpResponse(FaliureCode)
    user = User.objects.get(Email = request.session['email'])
    post = Post.objects.create(Title=request.POST['title'],Content=request.POST['content'],Author=user,Date=timezone.now())
    post.save()
    return HttpResponse(SuccessCode)
