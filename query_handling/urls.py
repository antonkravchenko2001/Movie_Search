from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('search/', views.search_results_view, name='search_results'),
    path('find/<int:idx>/',  views.movie_info_view, name='movie_info'),
    path('autocomplete_rest/', views.autocomplete_view, name='autocomplete'),
    path('addmovies/', views.post_movie_view, name='movies_post'),
    path('about/', views.about_view, name='about_page')
]