from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from apps.user.models.user import User, History
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_list_or_404
from api.user.serializers import (
    UserSerializer, 
    UserGetSerializer,
    CustomTokenObtainPairSerializer,
    HistorySerializer,
    HistoryCreateSerializer
) 



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]



class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserGetSerializer

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserGetSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HistoryCreateAPIView(generics.CreateAPIView):
    queryset = History.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = HistoryCreateSerializer

class HistoryListAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = HistorySerializer

    def get_queryset(self):
        authenticated_user = self.request.user
        return get_list_or_404(History, user=authenticated_user.id)

class HistoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = History.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = HistorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)