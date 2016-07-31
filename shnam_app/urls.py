from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
	
	url(r'^$', views.main, name='main'),
	url(r'^login__page', views.login__page, name='login__page'),
	url(r'^login', views.login, name='login'),
	url(r'^search_friends', views.search_friends, name='search_friends'),
]