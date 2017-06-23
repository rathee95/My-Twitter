# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
from rest_framework import serializers
from tweets.models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweet
		fields = ['user','content']