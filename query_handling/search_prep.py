from algorithms.search.search_models import SymmetricModel, AsymmetricModel
from algorithms.autocomplete.trie import Trie
from .models import MoviesInfo


def search(query, num_return = 20):
    trie = Trie()
    containes_query = trie.has_word(query)
    if containes_query:
        query = containes_query
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
    res['countries'] = eval(movie.countries)
    res['genre'] = eval(movie.genre)
    res['plot'] = movie.plot
    return res


def prepare_date(date):
    if date:
        cleaned_date = date.split('-')
        print(cleaned_date)
        return cleaned_date[0]
    return date