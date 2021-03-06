# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal



class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)
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
    likes = models.IntegerField(default=0)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    waypts = models.TextField()
    liked_by=models.ManyToManyField(User, related_name = "route_liked_by")
    created_by=models.ForeignKey(User, related_name = "route_created_by")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.likes<0:
            self.likes=0
        super(Route, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)



    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=user)
