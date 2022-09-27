from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('news/', views.news, name='news'),
    path('players/', views.players, name='players'),
    path('makepost/', views.make_post, name='make_post'),
    path('<int:post_id>/', views.show_post, name='show_post'),
    path('players/<int:post_id>', views.show_post, name='show_post'),
    path('news/<int:post_id>', views.show_post, name='show_post'),
    path('games/<int:post_id>', views.show_post, name='show_post'),
    path('makepost/<int:post_id>', views.show_post, name='show_post'),
]
