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

    def paginated_search(self, query, per_page=10, current_page=1):
        results = self.search(query)

    def searchable_models(self):
        return [(Movie, "title"), (Actor, "name")]

    def _model_search(self, model, attribute, query):
        return model.query.filter(getattr(model, attribute).like("%" + query + "%")).all()


y = crypt(x, salt)
