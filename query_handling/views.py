from algorithms.autocomplete.trie import Trie
from .search_prep import search, find
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import MoviesForm


def home_view(request):
    return render(
            request,
            'query_handling/home.html',
            )


def search_results_view(request):
    if 'query' in request.GET.keys() and request.GET['query']:
        query = request.GET['query']
        init_query = query
        search_results = search(query)
        return render(
            request,
            'query_handling/search_results.html',
            {'search_results': search_results, "query": init_query})

    elif 'selection' in request.GET.keys() and request.GET['selection']:
        query = request.GET['selection']
        init_query = query
        trie = Trie()
        word_count = trie.update_root(query)
        search_results = search(query)
        return render(
            request,
            'query_handling/search_results.html',
            {'search_results': search_results, "query": init_query})
    else:
        return render(
            request,
            'query_handling/404_error.html')


def movie_info_view(request, idx):
    movie = find(idx)
    return render(
        request,
        'query_handling/movie_info.html',
        {'movie': movie}
    )


def post_movie_view(request):
    form = MoviesForm()
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addmovies')
    return render(request, 'query_handling/post_movie.html', {'form': form})


def about_view(request):
    return render(request, 'query_handling/about.html')


@api_view(['GET'])
def autocomplete_view(request):
    if 'q' in request.GET.keys():
        if request.GET['q']:
            phrase = request.GET['q']
        else:
            phrase = ""
        print(phrase)
        trie = Trie()
        return Response({'matches': trie.match_prefix(phrase)})
