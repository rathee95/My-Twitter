from .views import TweetListAPIView, TweetCreateAPIView
 # TweetDetailView,TweetDeleteView ,  ,TweetUpdateView, TweetCreateView
from django.conf.urls import url
from django.views.generic.base import RedirectView



urlpatterns = [
	# url(r'^$', RedirectView.as_view(url="/")), #redirects to home 
		url(r'^$', TweetListAPIView.as_view(),name = 'list'), #redirects to home 
		url(r'^create/$', TweetCreateAPIView.as_view(),name = 'create'), #redirects to home 
	# url(r'^search/$', TweetListView.as_view(),name="list"),
 #    url(r'^create/$', TweetCreateView.as_view(),name="create"),
 #    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name="detail"), #pk --> dynamic url routing
 #    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),name="update"), #pk --> dynamic url routing
 #    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(),name="delete"), 
]