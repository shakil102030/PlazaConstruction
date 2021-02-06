from django.db import models
from django.utils.safestring import mark_safe
from Construct.models import ConstructionCategory

class Services(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length = 200)
    tileicon = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'services/')
    details = models.TextField()
    status = models.CharField(max_length = 40, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Teams(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    name = models.CharField(max_length = 200)
    es_category = models.ForeignKey(ConstructionCategory, on_delete = models.CASCADE)
    facebook_url = models.URLField(blank = True, max_length = 200, null=True)
    instagram_url = models.URLField(blank = True, max_length = 200, null=True)
    twitter_url = models.URLField(blank = True, max_length = 200, null=True)
    linkedin_url = models.URLField(blank = True, max_length = 200, null=True)
    image = models.ImageField(upload_to = 'team_member/')
    details = models.TextField()
    status = models.CharField(max_length = 40, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heigths="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'image'



