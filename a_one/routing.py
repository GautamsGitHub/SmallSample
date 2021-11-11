from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/a_one/<str:board_number>/', consumers.BoardConsumer.as_asgi()),
]