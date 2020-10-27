from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    body = models.CharField(max_length=4000)
    STATUS_OPTIONS = (
        ('D', 'Draft'),
        ('P', 'Publish'),
    )
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE)
    updated_by=models.ForeignKey(User, related_name='updated_by_user', on_delete=models.CASCADE)

