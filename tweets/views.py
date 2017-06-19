from django import forms 
from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView , DeleteView,ListView , CreateView ,UpdateView
from .forms import TweetModelForm
from django.forms.utils import ErrorList
from .mixins import FormUserNeededMixin , UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
#CRUD List/Search


class TweetCreateView(FormUserNeededMixin,CreateView):
	form_class  = TweetModelForm
	template_name = "tweets/create_view.html"
	# success_url = "/tweet/create/" # if not mentioned by default get_absolute_url mentioned in models.py
	# login_url = "/admin/" (LoginRequiredMixin if this is added)


	#done in mixins.py FormUserNeededMixin
	# def form_valid(self,form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView,self).form_valid(form)
	# 	else:
			
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in"])
	# 		return self.form_invalid(form)

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	# success_url = "/tweet/"
	template_name = "tweets/update_view.html"


class TweetDetailView(DetailView):
	# template_name = "tweets/detail_view.html" #tweet_detail.html
	queryset = Tweet.objects.all()

	#managed by django itself !!! 
	# def get_object(self):
	# 	pk = self.kwargs.get("pk") # obtained from url 
	# 	return Tweet.objects.get(id = pk)

class TweetListView(ListView):
	# template_name = "tweets/list_view.html" #tweet_list.html
	def get_queryset(self , *args , **kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get("q",None)
		if query is not None:
			qs = qs.filter(
				Q (content__icontains = query ) | 
				Q (user__username__icontains = query )
				)
		return qs

#now how do the template gets "context" from the class based views?
	# def get_context_data() -->see documentation


class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model = Tweet
	template_name="tweets/delete_confirm.html"
	success_url = reverse_lazy("tweet:list")










#################################################################
# #function based views
# def tweet_detail_view(request,id = 1):
# 	obj = Tweet.objects.get(id=id)
# 	context = {"object": obj }
# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	context = {"object_list": queryset}
# 	return render(request, "tweets/list_view.html", context)	
##################################################################	