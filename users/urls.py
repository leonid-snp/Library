from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='destroy'),
    path('list/', UserListAPIView.as_view(), name='list')
]
