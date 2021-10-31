from django.http.request import QueryDict
from rest_framework.serializers import Serializer
from algorithms.search.search_models import SymmetricModel, AsymmetricModel
from algorithms.autocomplete.trie import Trie
from django.shortcuts import redirect, render
from query_handling.models import MoviesInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import MoviesForm


def title_view(request):
    return render(
            request,
            'query_handling/search_templates/query_form.html',
            )

def search_movies(request):
    if 'query' in request.GET.keys() and request.GET['query']:
        query = request.GET['query']
        search_results = search(query)
        return render(
            request,
            'query_handling/search_templates/search_results.html',
            {'search_results': search_results})

    elif 'selection' in request.GET.keys() and request.GET['selection']:
        query = request.GET['selection']
        trie = Trie()
        word_count = trie.update_root(query)
        print(word_count)
        search_results = search(query)
        return render(
            request,
            'query_handling/search_templates/search_results.html',
            {'search_results': search_results})
    else:
        return render(
            request,
            'query_handling/errors/404_error.html')


def find_movie_info(request, idx):
    movie = find(idx)
    return render(
        request,
        'query_handling/info_templates/movie_info.html',
        {'movie': movie}
    )


def add_movie_info(request):
    form = MoviesForm()
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addmovies')
    return render(request, 'query_handling/post_templates/movie_form.html', {'form': form})


@api_view(['GET'])
def get_autocomplete(request):
    if 'q' in request.GET.keys():
        if request.GET['q']:
            phrase = request.GET['q']
        else:
            phrase = ""
        print(phrase)
        trie = Trie()
        return Response({'matches': trie.match_prefix(phrase)})


def search(query, num_return = 20):
    trie = Trie()
    if trie.has_word(query):
        search_model = SymmetricModel()
        model = search_model.model
        index = search_model.index
        query = MoviesInfo.objects.get(title=query).plot
        v = model(query).flatten()
    else:
        search_model = AsymmetricModel()
        model = search_model.model
        index = search_model.index
        v = model([query]).flatten()
    ids = index.get_nns_by_vector(v, num_return)
    output = {}
    for i, id in enumerate(ids):
        res = find(id)
        output[i] = res
    return output


def find(id:int) -> dict:
    movie = MoviesInfo.objects.get(id=id)
    res = {}
    res['id'] = movie.id
    res['movie_id'] = movie.movie_id
    res['title'] = movie.title
    res['release_date'] = prepare_date(movie.release_date)
    res['duration'] = movie.duration
    res['box_office'] = movie.box_office
    res['countries'] = movie.countries
    res['genre'] = movie.genre
    res['plot'] = movie.plot
    return res


def prepare_date(date):
    if date:
        cleaned_date = date.split('-')
        print(cleaned_date)
        return cleaned_date[0]
    return date
