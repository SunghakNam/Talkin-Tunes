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
	return render(request, 'login__page.html', {})

@ensure_csrf_cookie
def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')

	user = User(email=email, password=pbkdf2(sha256(str(password)).hexdigest()))
	user.__publish__()
	return HttpResponse(
            json.dumps(True),
            content_type="application/json")
