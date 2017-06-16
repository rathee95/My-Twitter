from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView , ListView
# Create your views here.
#CRUD List/Search


class TweetDetailView(DetailView):
	# template_name = "tweets/detail_view.html" #tweet_detail.html
	queryset = Tweet.objects.all()

	#managed by django itself !!! 
	# def get_object(self):
	# 	pk = self.kwargs.get("pk") # obtained from url 
	# 	return Tweet.objects.get(id = pk)

class TweetListView(ListView):
	# template_name = "tweets/list_view.html" #tweet_list.html
	queryset = Tweet.objects.all()

#now how do the template gets "context" from the class based views?
	# def get_context_data() -->see documentation

















#################################################################
#function based views
def tweet_detail_view(request,id = 1):
	obj = Tweet.objects.get(id=id)
	context = {"object": obj }
	return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	context = {"object_list": queryset}
	return render(request, "tweets/list_view.html", context)	
##################################################################	