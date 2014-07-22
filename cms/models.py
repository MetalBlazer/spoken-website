from django.db import models
from django.contrib.auth.models import User
from events.models import State, District, City, Location
import os

class Profile(models.Model):
    user = models.ForeignKey(User)
    confirmation_code = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(Location, null=True)
    district = models.ForeignKey(District, null=True)
    city = models.ForeignKey(City, null=True)
    state = models.ForeignKey(State, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'cms'

class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    permalink = models.CharField(max_length=255, unique=True)
    target_new = models.BooleanField()
    visible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

class Block_Location(models.Model):
    name = models.CharField(max_length=255)
    visible = models.BooleanField()

    def __unicode__(self):
        return self.name

class Block(models.Model):
    block_location = models.ForeignKey(Block_Location)
    title = models.CharField(max_length=255)
    body = models.TextField()
    position = models.IntegerField()
    visible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

class Nav(models.Model):
    nav_title = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    position = models.IntegerField()
    target_new = models.BooleanField()
    visible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

class SubNav(models.Model):
    nav = models.ForeignKey(Nav)
    subnav_title = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    position = models.IntegerField()
    target_new = models.BooleanField()
    visible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

class SiteFeedback(models.Model):
    name = models.CharField(max_length = 255)
    email =  models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
class Event(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 255)
    message = models.TextField()
    source_link = models.URLField(max_length=255, null=True, blank=True)
    event_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

class NewsType(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name
        
def content_file_name(instance, filename):
    ext = os.path.splitext(filename)[1]
    ext = ext.lower()
    return '/'.join(['news', str(instance.id), str(instance.id) + ext])

class News(models.Model):
    news_type = models.ForeignKey(NewsType)
    title = models.CharField(max_length = 255)
    picture = models.FileField(upload_to=content_file_name, null=True, blank=True)
    body = models.TextField()
    url = models.URLField(null=True, blank=True)
    url_title = models.CharField(max_length = 200, null=True, blank=True)
    created_by = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = "New"
