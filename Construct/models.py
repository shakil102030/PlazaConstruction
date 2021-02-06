from django.db import models
from django.utils.safestring import mark_safe


class ConstructionCategory(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length = 155)
    keywords = models.CharField(max_length = 100)
    details = models.TextField()
    image = models.ImageField(blank = True, upload_to = 'construct_category/')
    status = models.CharField(max_length = 20, choices = STATUS)
    slug = models.SlugField(null = True, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
        
class ConstructionArchitects(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    names = models.CharField(max_length = 155)
    keywords = models.CharField(max_length = 100)
    details = models.TextField()
    image = models.ImageField(blank = True, upload_to = 'architect_image/')
    status = models.CharField(max_length = 20, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.names


class ConstructionProjects(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(ConstructionCategory, on_delete = models.CASCADE)
    cons_architect = models.ForeignKey(ConstructionArchitects, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    keywords = models.CharField(max_length = 100)
    location = models.CharField(max_length = 200)
    manufactures = models.CharField(max_length = 200) 
    new_price = models.DecimalField(decimal_places = 2, max_digits = 15, default = 0)
    old_price = models.DecimalField(decimal_places = 2, max_digits = 15)
    amount = models.IntegerField(default = 0)
    min_amount = models.IntegerField(default = 3)
    details = models.TextField()
    image = models.ImageField(blank = True, upload_to = 'construct_projects/')
    status = models.CharField(max_length = 20, choices = STATUS)
    slug = models.SlugField(null = True, unique = True)
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



class Images(models.Model):
    projects = models.ForeignKey(ConstructionProjects, on_delete = models.CASCADE)
    title = models.CharField(blank = True, max_length = 200)
    image = models.ImageField(blank = True, upload_to = 'projects_images/')

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
