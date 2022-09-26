from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('news/', views.controversies, name='news'),
    path('players/', views.players, name='players'),
    path('makepost/', views.make_post, name='make_post'),
    path('<int:post_id>', views.show_post, name='show_post'),
    path('search_value', views.search_value, name='search_value'),
]
