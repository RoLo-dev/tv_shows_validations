from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = 'Please add a title'
        if len(postData['network']) < 2:
            errors['network'] = 'Please fill in the network field'
        if len(postData['release_date']) < 2:
            errors['release_date'] = 'Please add the release date'
        if len(postData['desc']) < 1:
            errors['desc'] = 'Please add a description'
        return errors

class Show(models.Model): 
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=150)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()