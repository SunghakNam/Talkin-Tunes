# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.hashers import *
from models import *
from shnam.lib.pbkdf2 import pbkdf2
from hashlib import sha256
from django.http import *
import json
def main(request):
	return render(request, 'index.html', {})

# login
def login__page(request):
	return render(request, 'login__page.html', {})

@ensure_csrf_cookie
def login(request):
	try:
		email = request.POST.get('email')
		password = request.POST.get('password')
		if User.objects.filter(email=email).exists():
			user = User.objects.get(email=email)
			if User.check_password(user, sha256(password).hexdigest()):
				login_status = {'result': True}
				request.session.delete()
		else:
			user = User(email=email, password=pbkdf2(sha256(str(password)).hexdigest()))
			user.__publish__()

		request.session['email'] = user.email
		return HttpResponse(
	            json.dumps(login_status),
	            content_type="application/json")
	except:
		login_status = {'result': False}
		return HttpResponse(
	            json.dumps(login_status),
	            content_type="application/json")

@ensure_csrf_cookie
def login_check(request):
	print request.session
	return 0 

def search_friends(request):
	users = User.objects.filter(email__contains=request.POST.get('friends_info')).exclude(email=request.session['email'])
	return render(request, 'search_friends_list.html', {'users': users})

def get_friends(request):
	user = this_user(request)
	friends = Friend.objects.filter(sender=user, disable=0)
	print friends
	return render(request, 'friends_list.html', {'friends': friends, 'uri': request.POST.get('uri')})	

def add_friend(request):
	try:
		user = this_user(request)
		friend_id = request.POST.get('friendIdx')
		friend = User.objects.get(userIdx=friend_id)
		friend_obj = Friend(sender=user, receiver=friend)
		friend_obj.__publish__()
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")

def this_user(request):
	user_email = request.session['email']
	user = User.objects.get(email=user_email)
	return user









