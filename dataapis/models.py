from django.db import models
from django.utils import timezone

# Create your models here.
class OutdoorDate(models.Model):
  title = models.CharField(max_length=200)
  place = models.CharField(max_length=200)
  date = models.DateField(default = timezone.now)
  description = models.CharField(max_length=200)
  comments = models.CharField(max_length=200, blank=True)
  
  picture = models.ImageField(blank=True, upload_to='')
  
  owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
  
  class Meta:
    ordering = ['-date']
  
  def __str__(self):
    return self.title