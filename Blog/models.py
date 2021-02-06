from django.db import models
from django.utils.safestring import mark_safe
from Construct.models import ConstructionCategory

class BlogGrid(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length = 200)
    cons_category = models.ForeignKey(ConstructionCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'blog/')
    details = models.TextField()
    status = models.CharField(max_length = 40, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heigths="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'image'

