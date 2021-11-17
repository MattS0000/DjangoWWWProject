from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('snake/', views.snake_render, name="snake"),
    path('game2/', views.game2, name="game2"),
    path('game3/', views.game3, name="game3"),
    path('register/', views.register_request, name='register'),
    path('flappy/', views.temp_flap, name='temp_flappy'),
    path('temp_snake/', views.temp_snake, name='temp_snake'),
]