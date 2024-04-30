from rest_framework import serializers
from apps.game.models.category import Category
from apps.game.models.question import Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'count',
            'time',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'category',
            'image'
        ]

class QuestionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'category'
        ]

class QuestionidsSerializer(serializers.Serializer):
    question_ids = serializers.ListField(child=serializers.IntegerField())

class QuestionGetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'image'
        ]