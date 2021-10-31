from django.urls import path
from . import views

urlpatterns = [
    path('', views.title_view, name='title_page'),
    path('search/', views.search_movies, name='search_results'),
    path('find/<int:idx>/',  views.find_movie_info, name='movie_info'),
    path('autocomplete_rest/', views.get_autocomplete, name='autocomplete'),
    path('addmovies/', views.add_movie_info, name='movies_submit')
]