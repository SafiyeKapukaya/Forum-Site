from django.shortcuts import get_object_or_404, redirect, render
from .decorators import unauthorized_user
from home.forms import UserRegisteration
from .models import Author,Post,Reply
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditPostForm, PostForm, ReplyForm

def home(request):
    return render(request,'forum/base.html')
def mainpage(request):
    return render(request,"forumone/index.html")

def threads(request):
    return render(request,'forum/post.html')

def thread_list(request):
    thread_list = Post.objects.select_related('user').all().values('id', 'user__name', 'user__lastname', 'content', 'postdate')
    sablon = loader.get_template('forumone/posts.html')
    veriler = {
        'thread_list' : thread_list,
        
    }
    return HttpResponse(sablon.render(veriler,request))

@unauthorized_user
def login_view(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('username')
        sifre = request.POST.get('password')
        user = authenticate(request,username = kullanici_adi , password = sifre)
        if user is not None:
            login(request,user)
            return redirect("threadlist")
        else:
            messages.info(request,'username or password is incorrect')
    
    return render(request,'forum/login.html')


def logout_view(request):
    logout(request)
    return render(request,"forum/base.html")

def profile(request):
    return render(request,'forum/profile.html')

@unauthorized_user
def register_view(request):
    form = UserRegisteration()
    if request.method=='POST':
        form =UserRegisteration(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            messages.info(request,username+'Your account is created')
            Author.objects.create(user=user,name=username,lastname='')
            return redirect('login')
        
    context={'form':form}
    
    return render(request,'forum/register.html',context)

@csrf_exempt
@login_required
def createpost(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("threadlist")
        else:
            print("form not valid")
            print(form.errors)
    context.update({
        "form": form,
        "title": "OZONE: Create New Post"
    })
    return render(request, "forumone/addthread.html", context)


@login_required
def create_reply(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    form = ReplyForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user_name = request.user.first_name
            user_lastname = request.user.last_name
            author, created = Author.objects.get_or_create(
            user=request.user,
            defaults={'name': user_name, 'lastname': user_lastname},
        )
            
            new_reply = form.save(commit=False)
            new_reply.user = author
            new_reply.post = post
            new_reply.save()
            reply_list = Reply.objects.filter(post=post).values('id', 'user__user__username', 'content', 'replydate')
            context['reply_list'] = reply_list

            return redirect("threadlist")
    print(f"post_id: {post_id}")
    print(f"post: {post}")

    context.update({
        "form": form,
        "post": post,
        "title": "OZONE: Create New Reply"
    })
    return render(request, "forumone/addreply.html", context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user.user:
        post.delete()
        return redirect("threadlist")
    else:
        return redirect("threadlist")
    
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("threadlist")
    else:
        form = EditPostForm(instance=post)

    return render(request, 'forumone/editpost.html', {'form': form, 'post': post})





