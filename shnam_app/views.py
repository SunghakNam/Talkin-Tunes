from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.hashers import *
from models import *
from pbkdf2 import *
from hashlib import sha256
from django.http import *

def main(request):
	return render(request, 'index.html', {})

# login
def login__page(request):
	return render(request, 'login__page.html', {})

@ensure_csrf_cookie
def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	import random
	pas1 = pbkdf2(sha256(str(password)).hexdigest(), salt=8, iterations=10000)
	pas2 =  pbkdf2(sha256('0326skace').hexdigest(), salt=8, iterations=10000)
	print pas1, pas2
	print pas1 == pas2
	#print type(str(PBKDF2(sha256(str(password)).hexdigest(), salt=str(random.randrange(0,8)))))
	#print type(PBKDF2(sha256(str(password)).hexdigest(), salt=str(random.randrange(0,8))))
	user = User(userId= '666', email=email, password=pbkdf2(sha256(str(password)).hexdigest(), salt=str(random.randrange(0,8)), iterations=10000))

	user.__publish__()
	#print set_password(password)
	return HttpResponse(
            json.dumps(True),
            content_type="application/json")
