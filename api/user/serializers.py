from rest_framework import serializers
from apps.user.models.user import User, History
from api.game.serializers import CategorySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['id'] = str(user.id)
        return token
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
        ]

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        return User.objects.create(**validated_data, password = password)
           

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'is_superuser',
        ]


class HistorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = History
        fields = [
            'id',
            'count',
            'user',
            'category',
            'time',
            'is_win',
        ]

class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'id',
            'count',
            'user',
            'category',
            'time',
            'is_win',
        ]