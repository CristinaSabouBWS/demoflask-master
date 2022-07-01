from flask import Flask, request

from presenter.models.movie import Movie
from presenter.models.actor import Actor
import ipdb


class Search:
    def __init__(self):
        self.results = dict()

    def search(self, query=""):
        if self.results == dict():
            for model, attribute in self.searchable_models():
                self.results[model.__tablename__] = self._model_search(model, attribute, query)
        return self.results

    def searchable_models(self):
        return [(Movie, "title"), (Actor, "name")]

    def _model_search(self, model, attribute, query):
        return model.query.filter(getattr(model, attribute).like("%" + query + "%")).all()

    def paginated_search(self, query, per_page=5, current_page=1):
        search_result = self.search(query)
        movie_mess = ""
        actors_mess = ""
        per_page = request.args.get("items", 5, type=int)
        current_page = request.args.get("page", 1, type=int)
        movie_result = search_result["movies"]
        actors_result = search_result["actors"]
        if movie_result == []:
            movie_mess = f"No movies for query {query}"
        if actors_result == []:
            actors_mess = f"No actors for query {query}"

        movie_count = len(movie_result)
        actors_count = len(actors_result)
        start = per_page * (int(current_page) - 1)
        movie_end = min(start + per_page, movie_count)
        actors_end = min(start + per_page, actors_count)
        movies = movie_result[start:movie_end]
        actors = actors_result[start:actors_end]
        search_result["movies"] = movies
        search_result["actors"] = actors
        search_result["per_page"] = per_page
        search_result["current_page"] = current_page
        search_result["movie_mess"] = movie_mess
        search_result["actors_mess"] = actors_mess
        return search_result
