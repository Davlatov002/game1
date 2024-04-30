from rest_framework.urls import path
from api.game.views import (
    CategoryListAPI,
    CategoryRetrieveAPI,

    QuestionlistAPIView,
    QuestionRetrieveAPI,
    QuestionlistImageAPIView,
    
)

urlpatterns = [
    path('categorys/', CategoryListAPI.as_view(), name='categorys_list'),
    path('category/<int:pk>/', CategoryRetrieveAPI.as_view(), name='category_retrieve'),

    path('questions/<int:pk>',QuestionlistAPIView.as_view(), name='questions_list'),
    path('question/<int:pk>',QuestionRetrieveAPI.as_view(), name='questions_retrieve'),
    path('questions-image/',QuestionlistImageAPIView.as_view(), name='questions_image_list'),

]