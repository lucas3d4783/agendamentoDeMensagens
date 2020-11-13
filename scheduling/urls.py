from rest_framework.routers import DefaultRouter
from .views import SchedulingViewSet, SocialNetworkViewSet
from . import views
from django.urls import path, include


r = DefaultRouter()
r.register(r'', SchedulingViewSet)
schedulings_urls = r.urls

router = DefaultRouter()
router.register(r'', SocialNetworkViewSet)
social_networks_urls = router.urls
