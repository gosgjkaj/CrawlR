# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal



class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Route(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique = True)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    waypts = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Route, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)



    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
