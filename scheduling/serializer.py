from rest_framework import serializers
from scheduling.models import Scheduling, SocialNetwork

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['id', 'name']

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling 
        fields = '__all__'
