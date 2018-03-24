from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
