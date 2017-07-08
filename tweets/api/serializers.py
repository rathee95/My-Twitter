# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class ParentTweetModelSerializer(serializers.ModelSerializer):
	
	user = UserDisplaySerializer(read_only = True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()

	class Meta:
		model = Tweet
		fields = ['id','user','content','timestamp','date_display','timesince','did_like','likes',]

	def get_did_like(self, obj):
		request = self.context.get('request')
		user = request.user
		if user.is_authenticated():
			if user in obj.liked.all():
				return True
		return False


	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d %Y, %I:%M %p")

	def get_timesince(self,obj):
		return timesince(obj.timestamp) + " ago"

	def get_likes(self,obj):
		return obj.liked.all().count()

				


class TweetModelSerializer(serializers.ModelSerializer):
	parent_id = serializers.CharField(write_only=True, required=False)
	user = UserDisplaySerializer(read_only = True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent = ParentTweetModelSerializer(read_only = True)
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()
	
	class Meta:
		model = Tweet
		fields = ['parent_id','id','user','content','timestamp','date_display','timesince','parent','did_like','likes','reply']
	
	def get_did_like(self, obj):
		request = self.context.get('request')
		user = request.user
		if user.is_authenticated():
			if user in obj.liked.all():
				return True
		return False
				


	def get_likes(self,obj):
		return obj.liked.all().count()

	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d %Y, %I:%M %p")
	def get_timesince(self,obj):
		return timesince(obj.timestamp) + " ago"


