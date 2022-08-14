from django.contrib import admin
from .models import *

admin.site.register(Clans, Member, League, War, Battle, League_grade)
