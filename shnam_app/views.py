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
def login_page(request):
	return render(request, 'login_page.html', {})

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
	if 'email' in request.session:
		login_status = {"result": True}
	else:
		login_status = {"result": False}
	return HttpResponse(json.dumps(login_status), content_type="application/json")

def logout(request):
	try:
		request.session.delete()
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")

#page nav
def feed_page(request):
	user = this_user(request)
	feed_list = None
	#music sent
	musicmsg = MusicMsg.objects.filter(followObj__followee=user)

	#follow request
	fol_request = Follow.objects.filter(followee=user)

	from itertools import chain
	from operator import attrgetter
	feed_list = sorted(chain(musicmsg, fol_request), key=attrgetter('createdTime'))
	return render(request, 'feed_page.html', {'feed_list': feed_list, 'width': request.POST.get('width')})

def my_page(request):
	if request.POST.get('userinfo') == 'true':
		user = User.objects.get(email=request.POST.get('user'))
		logout_enable = False
	else:
		user = this_user(request)
		logout_enable = True
	following = Follow.objects.filter(follower=user, disable=0)
	followed = Follow.objects.filter(followee=user, disable=0)
	playlist = Playlist.objects.filter(user=user, disable=0)
	return render(request, 'my_page.html', {'user': user, 'following_num':following.count(), 'followed_num': followed.count(),'playlist':playlist, 'width':request.POST.get('width'), 'logout_enable':logout_enable})

def search_friends(request):
	users = User.objects.filter(email__contains=request.POST.get('friends_info')).exclude(email=request.session['email'])
	following = Follow.objects.filter(follower=this_user(request), disable=0).values_list('followee_id')
	if following:
		following = following[0]
	return render(request, 'search_friends_list.html', {'users': users, 'following': following})

def get_friends(request):
	user = this_user(request)
	follows = Follow.objects.filter(follower=user, disable=0)
	return render(request, 'friends_list.html', {'follows': follows, 'uri': request.POST.get('uri')})	

def add_friend(request):
	try:
		user = this_user(request)
		followee_id = request.POST.get('friendIdx')
		followee = User.objects.get(userIdx=followee_id)
		if Follow.objects.filter(follower=user, followee=followee).exists():
			Follow.objects.filter(follower=user, followee=followee).update(disable=0)
		else:
			follow_obj = Follow(follower=user, followee=followee)
			follow_obj.__publish__()
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")

def remove_friend(request):
	try:
		user = this_user(request)
		followee_id = request.POST.get('friendIdx')
		followee = User.objects.get(userIdx=followee_id)
		follow_obj = Follow.objects.filter(follower=user, followee=followee).update(disable=1)
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")


def send_music(request):
	try:
		uri = request.POST.get('uri')
		receiverId = request.POST.get('receiver')
		receiver = User.objects.get(userIdx=receiverId)
		sender = this_user(request)

		follow_obj = Follow.objects.get(follower=sender, followee=receiver)

		#create a message
		# musicmsg = MusicMsg(sender=sender,receiver=receiver,uri=uri)
		musicmsg = MusicMsg(followObj=follow_obj, uri=uri)
		musicmsg.__publish__()
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")		

def add_playlist(request):
	try:
		user = this_user(request)
		uri = request.POST.get('uri')

		if Playlist.objects.filter(user=user, uri=uri, disable=1).exists():
			Playlist.objects.filter(user=user, uri=uri, disable=1).update(disable=0)
		else:
			#add to a playlist
			playlist = Playlist(user=user, uri=uri)
			playlist.__publish__()
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")


def remove_playlist(request):
	try:
		user = this_user(request)
		pid = request.POST.get('pid')

		#get playlist
		playlist = Playlist.objects.filter(playlistIdx=pid, user=user).update(disable=1)
		return HttpResponse(json.dumps('success'), content_type="application/json")
	except:
		return HttpResponse(json.dumps('error'), content_type="application/json")	


def get_following(request):
	# import pdb; pdb.set_trace()
	user = this_user(request)
	following = Follow.objects.filter(follower=user)
	return render(request, 'follow.html', {'user': user, 'type':'following', 'follow': following})

def get_follower(request):
	user = this_user(request)
	follower = Follow.objects.filter(followee=user)
	return render(request, 'follow.html', {'user': user, 'type':'follower', 'follow': follower})

def error_report(request):
	user = "none"
	if request.session.has_key('email'):
		user = this_user(request)
	callFunc = request.POST.get('callFunc')
	status = request.POST.get('status')
	if request.POST.get('responseText'):
		responseText = request.POST.get('responseText')
	else: 
		responseText=u'Unknown';
	errmsg =request.POST.get('errmsg')
        
	ErrorReport(user=user.email,callFunc=callFunc,status=status,responseText=responseText,errmsg=errmsg).__publish__()
        
	return HttpResponse(json.dumps(True), content_type="application/json")

def this_user(request):
	user_email = request.session['email']
	user = User.objects.get(email=user_email)
	return user








