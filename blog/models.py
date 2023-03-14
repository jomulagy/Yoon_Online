from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #author:

    def __str__(self):
        return f'[{self.pk}],{self.title}'