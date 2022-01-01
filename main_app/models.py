from django.db import models
from django.urls import reverse

class Tama(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tamas_detail', kwargs={'tama_id': self.id})
