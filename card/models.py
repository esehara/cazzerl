from django.db import models

class Card(models.Model):
    contents = models.TextField(max_length=800)
    pub_data = models.DateTimeField('date published')

# Create your models here.
