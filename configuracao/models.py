from django.db import models

class Twitter(models.Model):

    usuario = models.CharField(max_length = 20)
    consumer_key = models.CharField(max_length = 100)
    consumer_secret = models.CharField(max_length = 100)
    access_key = models.CharField(max_length = 150)
    access_secret = models.CharField(max_length = 150)
