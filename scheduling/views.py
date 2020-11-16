from rest_framework import viewsets
from scheduling.models import Scheduling, SocialNetwork
from scheduling.serializer import SchedulingSerializer, SocialNetworkSerializer
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all() 
    serializer_class = SocialNetworkSerializer

    """@api_view(http_method_names=['DELETE'])
    def delete(request, pk):
        try:
            social_network = get_object_or_404(SocialNetwork, pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            operation = social_network.delete()

            if operation:
                return '{"success": "deletado com sucesso"}', 200
            else:
                return '{"error": "erro ao deletar"}', 500
"""

class SchedulingViewSet(viewsets.ModelViewSet):
    queryset = Scheduling.objects.all() 
    serializer_class = SchedulingSerializer

