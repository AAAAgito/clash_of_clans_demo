#coding=utf8
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClansSerializer, UserSerializer, GroupSerializer
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
        