from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title