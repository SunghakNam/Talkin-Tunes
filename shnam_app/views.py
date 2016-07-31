# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
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
	print Friends.objects.filter(friends_idx=1)
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
				request.session['email'] = user.email
		else:
			user = User(email=email, password=pbkdf2(sha256(str(password)).hexdigest()))
			user.__publish__()
		return HttpResponse(
	            json.dumps(login_status),
	            content_type="application/json")
	except:
		login_status = {'result': False}
		return HttpResponse(
	            json.dumps(login_status),
	            content_type="application/json")
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def search_friends(request):
	users = User.objects.filter(email__contains=request.POST.get('friends_info'))
	return render(request, 'friends_list.html', {'users': users})
