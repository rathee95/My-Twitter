import re

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save

from hashtags.signals import parsed_hashtags
 

class TweetManager(models.Manager):
	def retweet(self,user,parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj

		qs  = self.get_queryset().filter(user= user,parent = og_parent).filter(
			timestamp__year=timezone.now().year,
			timestamp__month=timezone.now().month,
			timestamp__day=timezone.now().day,

			)
		if qs.exists():
			return None # dont retweet what you have already retweeted !!

		obj = self.model(
				parent = og_parent,
				user = user,
				content = parent_obj.content,
			)
		obj.save()
		return obj

	def like_toggle(self,user,tweet_obj):
		if user in tweet_obj.liked.all():
			is_liked = False
			tweet_obj.liked.remove(user)
		else:
			is_liked = True
			tweet_obj.liked.add(user)	
		return is_liked

class Tweet(models.Model):
	parent = models.ForeignKey("self", blank = True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	content = models.CharField(max_length =140)
	liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank= True,related_name = 'liked')
	reply = models.BooleanField(verbose_name='Is a reply?',default= False)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = TweetManager()

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail" , kwargs= {"pk": self.pk})

	class Meta:
		ordering  = ['-timestamp']


#this runs whenever a tweet is created , sends notification to all users tagged with hashtags involved
def tweet_save_receiver(sender,instance,created,*args,**kwargs):
	if created and not instance.parent:#is not retweet

		user_regex = r'@(?P<username>[\w.@+-]+)'
		m = re.findall(user_regex,instance.content)
		#send notification here 

		hash_regex = r'#(?P<username>[\w.@+-]+)' 
		hashtags = re.findall(hash_regex,instance.content)
		parsed_hashtags.send(sender=instance.__class__,hashtag_list=hashtags)
		#send hashtag signal to user here 




post_save.connect(tweet_save_receiver, sender = Tweet)