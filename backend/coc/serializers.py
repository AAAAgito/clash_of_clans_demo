# -*- coding:utf-8 -*-
from collections import OrderedDict
from rest_framework import serializers
from .models import *

class ClansSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    class Meta:
        model = Clans
        fields = ('id', 'name', 'note', 'leader', 'group', )

class MemberSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields = ('id', 'clans_id', 'name', 'note', 'leader', 'group', )

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'clans_id', 'start_date','name',  )

class WarSerializer(serializers.ModelSerializer):
    class Meta:
        model = War
        fields = ('id', 'ordinal_id', 'belong_league_id', )

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ('id', 'belong_war_id', 'self_member_id', 
        'self_match_value', 'enemy_match_value', 'attack_stars', )

class League_gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'belong_league_id', 'self_member_id', 'attack_stars', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

