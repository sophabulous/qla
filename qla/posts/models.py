import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_author = models.CharField(max_length=30, default='firstname_lastname')
    post_category = models.CharField(max_length=15, default='category')
    post_title = models.CharField(max_length=100, default='title')
    post_excerpt = models.CharField(max_length=400, default='Lorem ipsum dolor')
    post_content = models.TextField(max_length=4000)
    post_thumb = models.CharField(max_length=30, default='fpo_square.PNG')
    post_cover = models.CharField(max_length=30, default='fpo_4x3.PNG')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
            return self.post_title + " by " + self.post_author
        
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class QLA(models.Model):
    qla_author = models.CharField(max_length=30, default='firstname_lastname')
    qla_title = models.CharField(max_length=100, default='title')
    qla_excerpt = models.CharField(max_length=400, default='Lorem ipsum dolor')
    qla_content = models.TextField(max_length=4000)
    qla_thumb = models.CharField(max_length=30, default='fpo_square.PNG')
    qla_date = models.DateTimeField('date published')
    
    def __str__(self):
            return self.qla_title + " by " + self.qla_author

class Contributor(models.Model):
    contributor_name = models.CharField(max_length=30, default='Firstname Lastname')
    contributor_image = models.CharField(max_length=30, default='img')
    contributor_position1 = models.CharField(max_length=20, default='')
    contributor_position2 = models.CharField(max_length=20, blank=True, default='')
    contributor_position3 = models.CharField(max_length=20, blank=True, default='')
    contributor_area1 = models.CharField(max_length=20, default='')
    contributor_area2 = models.CharField(max_length=20, blank=True, default='')
    contributor_area3 = models.CharField(max_length=20, blank=True, default='')
    contributor_biotext = models.TextField(max_length=3000, default='This contributor did not provide a bio')
    
    def __str__(self):
            return self.contributor_name

class SocialMediaIcon(models.Model):
    socialmediaicon_name = models.CharField(max_length=30, default='platform')
    socialmediaicon_normal = models.CharField(max_length=30, default='img')
    socialmediaicon_hover = models.CharField(max_length=30, default='hover_img')
    socialmediaicon_link = models.CharField(max_length=30, default='#')
    
    def __str__(self):
            return self.socialmediaicon_name

class WeeklyVignette(models.Model):
    weeklyvignette_title = models.CharField(max_length=100, default='title')
    weeklyvignette_author = models.CharField(max_length=30, default='firstname_lastname')
    weeklyvignette_excerpt = models.CharField(max_length=400, default='Lorem ipsum dolor')
    weeklyvignette_content = models.TextField(max_length=10000)
    weeklyvignette_cover = models.CharField(max_length=30, default='fpo_4x3.PNG')
    weeklyvignette_date = models.DateTimeField('date published')
    
    def __str__(self):
            return self.weeklyvignette_title + " by " + self.weeklyvignette_author