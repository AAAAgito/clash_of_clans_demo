# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,Group

class Clans(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 64)
    note = models.TextField()
    leader = models.IntegerField()
    group = models.ManyToManyField(Group, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    clans_id = models.IntegerField()
    name = models.CharField(max_length = 64)
    user = models.ManyToManyField(User, null=True, blank=True)
    group = models.ManyToManyField(Group, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class League(models.Model):
    id = models.IntegerField(primary_key=True)
    clans_id = models.IntegerField()
    start_date = models.DateField()
    name = models.CharField(max_length = 64)

    def __unicode__(self):
        return self.start_date

    class Meta:
        ordering = ['-id']

class War(models.Model):
    # range from 1~7, ordinal id
    id = models.IntegerField(primary_key=True)
    ordinal_id = models.IntegerField()
    belong_league_id = models.IntegerField()
    

    def __unicode__(self):
        return self.start_date

    class Meta:
        ordering = ['-id']

class Battle(models.Model):
    # range from 1~7, ordinal id
    id = models.IntegerField(primary_key=True)
    belong_war_id = models.IntegerField()
    self_member_id = models.IntegerField()
    self_match_value = models.IntegerField()
    enemy_match_value = models.IntegerField()
    attack_stars = models.IntegerField()


    def __unicode__(self):
        return self.start_date

    class Meta:
        ordering = ['-id']

class League_grade(models.Model):
    # range from 1~7, ordinal id
    id = models.IntegerField(primary_key=True)
    belong_league_id = models.IntegerField()
    self_member_id = models.IntegerField()
    attack_stars = models.IntegerField()


    def __unicode__(self):
        return self.start_date

    class Meta:
        ordering = ['-id']
