from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='amigos'),
    path('controversies/', views.controversies, name='familia'),
    path('players/', views.players, name='empresa'),
    path('makepost/', views.make_post, name='make_post'),
    path('<int:post_id>', views.show_post, name='show_post'),
]
