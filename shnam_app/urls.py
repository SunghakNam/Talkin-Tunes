from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
	
	url(r'^$', views.main, name='main'),

	#login
	url(r'^login_page', views.login_page, name='login_page'),
	url(r'^login_check', views.login_check, name='login_check'),
	url(r'^login', views.login, name='login'),
	url(r'^logout', views.logout, name='logout'),

	#page nav
	url(r'^feed_page', views.feed_page, name='feed_page'),
	url(r'^my_page', views.my_page, name='my_page'),

	#search friend and add
	url(r'^search_friends', views.search_friends, name='search_friends'),
	url(r'^get_friends', views.get_friends, name='get_friends'),
	url(r'^add_friend', views.add_friend, name='add_friend'),

	#send music
	url(r'^send_music', views.send_music, name='send_music'),

	#add to playlist
	url(r'^add_playlist', views.add_playlist, name='add_playlist'),
]