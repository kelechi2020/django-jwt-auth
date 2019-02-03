from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from music.views import ListSongsView, LoginView, RegisterUsers

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register")
]