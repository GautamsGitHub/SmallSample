from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name = "index"),
	path("<str:board_number>/", views.board, name = "board"),
]