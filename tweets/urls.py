from .views import TweetDetailView , TweetListView , TweetCreateView
from django.conf.urls import url

urlpatterns = [
	url(r'^$', TweetListView.as_view(),name="list"),
    url(r'^create/$', TweetCreateView.as_view(),name="create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name="detail"), #pk --> dynamic url routing

]
