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
router.register(r'leaguegrade', League_gradeViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^clansAPI', ClansAPIView.as_view()),
    url(r'^memberAPI', MemberAPIView.as_view()),
    url(r'^member_clansAPI', MemberFilterClansAPIView.as_view()),
    url(r'^leagueAPI', LeagueAPIView.as_view()),
    url(r'^league_clansAPI', LeagueFilterClansAPIView.as_view()),
    url(r'^warAPI', WarAPIView.as_view()),
    url(r'^war_leagueAPI', WarFilterLeagueAPIView.as_view()),
    url(r'^war_oridinalAPI', WarFilterOridinalAPIView.as_view()),
    url(r'^battleAPI', BattleAPIView.as_view()),
    url(r'^barttle_memberAPI', BattleFilterMemberAPIView.as_view()),
    url(r'^leaguegradeAPI', League_gradeAPIView.as_view()),
    url(r'^leaguegrade_memberAPI', League_gradeFilterMemberAPIView.as_view()),
    url(r'^leaguegrade_leagueAPI', League_gradeFilterLeagueAPIView.as_view()),
]
