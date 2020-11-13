from rest_framework import viewsets
from scheduling.models import Scheduling, SocialNetwork
from scheduling.serializer import SchedulingSerializer, SocialNetworkSerializer
from django.shortcuts import render, get_object_or_404, redirect


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all() 
    serializer_class = SocialNetworkSerializer

class SchedulingViewSet(viewsets.ModelViewSet):
    queryset = Scheduling.objects.all() 
    serializer_class = SchedulingSerializer

