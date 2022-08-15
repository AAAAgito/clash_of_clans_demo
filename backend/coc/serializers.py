# -*- coding:utf-8 -*-
from collections import OrderedDict
from rest_framework import serializers
from .models import *

class ClansSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    class Meta:
        model = Clans
        fields = ('id', 'name', 'note', 'leader', 'group', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

