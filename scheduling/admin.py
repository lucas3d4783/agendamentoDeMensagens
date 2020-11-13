from django.contrib import admin
from scheduling.models import SocialNetwork, Scheduling

admin.site.register([SocialNetwork, Scheduling])