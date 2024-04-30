from django.urls import path

from api.user.views import (
    CustomTokenObtainPairView,
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserListAPIView,

    HistoryCreateAPIView,
    HistoryListAPIView,
    HistoryRetrieveAPIView,
 
)

from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('user-create/', UserCreateAPIView.as_view(), name='user_create'),

    path('history/<int:pk>/', HistoryRetrieveAPIView.as_view(), name='history_retrieve'),
    path('historys/', HistoryListAPIView.as_view(), name='history_list'),
    path('history-create/', HistoryCreateAPIView.as_view(), name='history_create'),

]