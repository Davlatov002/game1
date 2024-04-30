from rest_framework import generics , response, status
from django.shortcuts import get_object_or_404, get_list_or_404
from api.game.serializers import QuestionSerializer, CategorySerializer, QuestionGetSerializer, QuestionGetImageSerializer, QuestionidsSerializer
from apps.game.models.question import Question
from apps.game.models.category import Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.user.models.user import User
import random

class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer


class CategoryRetrieveAPI(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class QuestionlistAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionGetSerializer

    def get_queryset(self):
        id = self.kwargs.get('pk')
        category = get_object_or_404(Category, id=id)
        category_questions = get_list_or_404(Question, category=id)
        
        count = category.count
        if count >= len(category_questions):
            random_questions = random.sample(category_questions, len(category_questions))
        else:
            random_questions = random.sample(category_questions, count)
        return random_questions


class QuestionlistImageAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionidsSerializer

    def post(self, request, *args, **kwargs):
        question_ids = request.data.get('question_ids', [])
        questions = get_list_or_404(Question, id__in=question_ids)
        serializer = QuestionGetImageSerializer(questions, many=True)
        question_count = len(serializer.data)
        if question_count >= 9:
            random_questions = random.sample(serializer.data, 9)
        else:
            random_questions = random.sample(serializer.data, question_count)
        return response.Response(random_questions)

    

class QuestionRetrieveAPI(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

