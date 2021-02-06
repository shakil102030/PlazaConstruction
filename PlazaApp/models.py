from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm, TextInput, EmailInput



class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length = 155)
    keywords = models.CharField(max_length = 250)
    description = models.CharField(max_length = 250)
    company = models.CharField(max_length = 50)
    address = models.CharField(blank = True, max_length = 100)
    phone = models.CharField(blank = True, max_length = 15)
    fax = models.CharField(blank = True, max_length = 15)
    email = models.CharField(blank = True, max_length = 50)
    smtpserver = models.CharField(blank = True, max_length = 50)
    smtpemail = models.CharField(blank = True, max_length = 50)
    smtppassword = models.CharField(blank = True, max_length = 50)
    smtpport = models.CharField(blank = True, max_length = 50)
    icon = models.ImageField(blank = True, upload_to = 'images/')
    facebook = models.URLField(blank = True, max_length = 50)
    instagram = models.URLField(blank = True, max_length = 50)
    twitter = models.URLField(blank = True, max_length = 50)
    youtube = models.URLField(blank = True, max_length = 50)
    aboutus = models.TextField(blank = True)
    contact = models.TextField(blank = True)
    references = models.TextField(blank = True)
    status = models.CharField(max_length = 10, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 40)
    subject = models.CharField(blank = True, max_length = 200)
    message = models.TextField(blank = True, max_length = 1000)
    ip = models.CharField(blank = True, max_length = 100)
    Note = models.CharField(blank = True, max_length = 200)
    status = models.CharField(max_length = 40, choices = STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name



class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'input', 'placeholder':'Name & Sure name'}),
            'email': EmailInput(attrs={'class':'input', 'placeholder':'Write your email'}),
            'message': TextInput(attrs={'class':'input', 'placeholder':'Write your message'}),
        } 












