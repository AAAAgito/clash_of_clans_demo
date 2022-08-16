#coding=utf8
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BattleSerializer, ClansSerializer, League_gradeSerializer, LeagueSerializer, MemberSerializer, UserSerializer, GroupSerializer, WarSerializer
from .base import BaseView
from .models import *


class UserViewSet(BaseView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(BaseView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ClansViewSet(BaseView):
    queryset = Clans.objects.all()
    serializer_class = ClansSerializer
    search_fields = ['id', ]

class MemberViewSet(BaseView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    search_fields = ['id', ]

class LeagueViewSet(BaseView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    search_fields = ['id', ]

class WarViewSet(BaseView):
    queryset = War.objects.all()
    serializer_class = WarSerializer
    search_fields = ['id', ]

class BattleViewSet(BaseView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    search_fields = ['id', ]

class League_gradeViewSet(BaseView):
    queryset = League_grade.objects.all()
    serializer_class = League_gradeSerializer
    search_fields = ['name', ]

class ClansAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        clans_data = Clans.objects.get(id = id)
        serializer = ClansSerializer(clans_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        clans_data = ClansSerializer(data=data)
        clans_data.is_valid(raise_exception=True)
        clans_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        clans_data = Clans.objects.get(id=id)
        ser = ClansSerializer(clans_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        Clans.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})
    
class MemberAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        member_data = Member.objects.get(id = id)
        serializer = MemberSerializer(member_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        member_data = Member(data=data)
        member_data.is_valid(raise_exception=True)
        member_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        member_data = member_data.objects.get(id=id)
        ser = MemberSerializer(member_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        Member.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})

class MemberFilterClansAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        member_data = Member.objects.filter(clans_id = id)
        serializer = MemberSerializer(member_data, many=True)
        return Response(serializer.data)


class LeagueAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        league_data = League.objects.get(id = id)
        serializer = LeagueSerializer(league_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        league_data = League(data=data)
        league_data.is_valid(raise_exception=True)
        league_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        league_data = league_data.objects.get(id=id)
        ser = LeagueSerializer(league_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        League.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})

class LeagueFilterClansAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        league_data = League.objects.filter(clans_id = id)
        serializer = LeagueSerializer(league_data, many=True)
        return Response(serializer.data)


class WarAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        war_data = War.objects.get(id = id)
        serializer = WarSerializer(war_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        war_data = War(data=data)
        war_data.is_valid(raise_exception=True)
        war_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        war_data = War.objects.get(id=id)
        ser = WarSerializer(war_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        War.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})

class WarFilterLeagueAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        war_data = War.objects.filter(belong_league_id = id)
        serializer = WarSerializer(war_data, many=True)
        return Response(serializer.data)

class WarFilterOridinalAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        war_data = War.objects.filter(ordinal_id = id)
        serializer = WarSerializer(war_data, many=True)
        return Response(serializer.data)


class BattleAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        battle_data = Battle.objects.get(id = id)
        serializer = BattleSerializer(battle_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        battle_data = Battle(data=data)
        battle_data.is_valid(raise_exception=True)
        battle_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        battle_data = Battle.objects.get(id=id)
        ser = BattleSerializer(battle_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        Battle.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})

class BattleFilterWarAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        battle_data = Battle.objects.filter(war_id = id)
        serializer = BattleSerializer(battle_data, many=True)
        return Response(serializer.data)

class BattleFilterMemberAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        battle_data = Battle.objects.filter(self_member_id = id)
        serializer = BattleSerializer(battle_data, many=True)
        return Response(serializer.data)


class League_gradeAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        league_grade_data = League_grade.objects.get(id = id)
        serializer = League_gradeSerializer(league_grade_data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        print(data)
        # function of actual stars
        league_grade_data = League_grade(data=data)
        league_grade_data.is_valid(raise_exception=True)
        league_grade_data.save()
        return Response({'code':1})

    def put(self,request):
        id = request.data.get("id")
        data = request.data
        league_grade_data = league_grade_data.objects.get(id=id)
        ser = League_gradeSerializer(league_grade_data,data=data)
        ser.is_valid()
        ser.save()
        return Response({"data": data, 'code': 0})
    # 删除
    def delete(self,request):
        id = request.query_params.get("id")
        League_grade.objects.filter(id=id).delete()
        return Response({'MSG':"删除成功","code":204})

class League_gradeFilterMemberAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        league_grade_data = League_grade.objects.filter(self_member_id = id)
        serializer = League_gradeSerializer(league_grade_data, many=True)
        return Response(serializer.data)

class League_gradeFilterLeagueAPIView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        league_grade_data = League_grade.objects.filter(belong_league_id = id)
        serializer = League_gradeSerializer(league_grade_data, many=True)
        return Response(serializer.data)
