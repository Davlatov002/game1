from django.urls import path, include

urlpatterns = [
    path('user/', include(('api.user.urls', 'apps.user'))),
    path('game/', include(('api.game.urls', 'apps.game'))),
]