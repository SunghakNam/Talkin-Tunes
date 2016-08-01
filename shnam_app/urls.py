from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
	
	url(r'^$', views.main, name='main'),
	url(r'^login__page', views.login__page, name='login__page'),
	url(r'^login', views.login, name='login'),

	##search friend and add
	url(r'^search_friends', views.search_friends, name='search_friends'),
	url(r'^get_friends', views.get_friends, name='get_friends'),
	url(r'^add_friend', views.add_friend, name='add_friend'),
]