from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=100)
    message_text = models.TextField()
    created_at = models.DateTimeField()

