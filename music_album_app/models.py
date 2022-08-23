from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    # release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #when item is saved, there will be a time stamp that can be used.

    def __str__(self):
        return f'{self.title}'
        