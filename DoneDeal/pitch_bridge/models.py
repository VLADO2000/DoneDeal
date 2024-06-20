from django.db import models
from uuid import uuid4
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(email='deleted@example.com')[0]


class Pitch(models.Model):
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid4())
    idea_description = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    idea_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET(get_sentinel_user))
    
    


