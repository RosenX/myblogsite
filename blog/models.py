from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return self.tag_name

class Author(models.Model):
    user = models.OneToOneField(User)
    qq =models.CharField(max_length=50,blank=True)
    website = models.URLField(max_length=100,blank=True)
    count = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.user.username

class Classification(models.Model):
    name = models.CharField(max_length=50)
    count =models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    visitedTime = models.PositiveIntegerField(default=0)
    classification = models.ForeignKey(Classification)
    author = models.ManyToManyField(Author,blank=True)

    def __unicode__(self):
        return self.caption

    class Meta:
        ordering = ['-publish_time']

class Comment(models.Model):
    """docstring for Comment"""
    publish_time =models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.TextField()
    blog = models.ForeignKey(Blog)
    parent = models.PositiveIntegerField(default=0)
    thread = models.CharField(max_length=100,unique=True)
    sonCnt = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return self.username

