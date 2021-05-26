from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  done = models.BooleanField()


  def __str__(self):
    return f"{self.title}"