from .views import TweetDetailView , TweetListView ,TweetUpdateView, TweetCreateView
from django.conf.urls import url

urlpatterns = [
	url(r'^$', TweetListView.as_view(),name="list"),
    url(r'^create/$', TweetCreateView.as_view(),name="create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name="detail"), #pk --> dynamic url routing
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),name="update"), #pk --> dynamic url routing

]
