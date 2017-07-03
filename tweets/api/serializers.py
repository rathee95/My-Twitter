# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class ParentTweetModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only = True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()

	class Meta:
		model = Tweet
		fields = ['id','user','content','timestamp','date_display','timesince']

	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d %Y, %I:%M %p")
	def get_timesince(self,obj):
		return timesince(obj.timestamp) + " ago"


class TweetModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only = True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent = ParentTweetModelSerializer(read_only = True)

	class Meta:
		model = Tweet
		fields = ['id','user','content','timestamp','date_display','timesince','parent']
	
	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d %Y, %I:%M %p")
	def get_timesince(self,obj):
		return timesince(obj.timestamp) + " ago"


