#coding=utf-8
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

# register的可选参数 base_name: 用来生成urls名字，如果viewset中没有包含queryset, base_name一定要有

router = DefaultRouter()
router.register(r'clans', ClansViewSet)
router.register(r'member', MemberViewSet)
router.register(r'league', LeagueViewSet)
router.register(r'war', WarViewSet)
router.register(r'battle', BattleViewSet)
router.register(r'league_grade', League_gradeViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^clansAPI', ClansAPIView.as_view()),
]
