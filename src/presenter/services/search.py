class SearchService:
    def search(self, query=""):
        results = dict()
        for model, attribute in self.searchable_models():
            results[model.__tablename__] = self._model_search(model, attribute, query)
        return results

    def searchable_models(self):
        from presenter.models.movie import Movie
        from presenter.models.actor import Actor

        return [(Movie, "title"), (Actor, "name")]

    def _model_search(self, model, attribute, query):
        return model.query.filter(getattr(model, attribute).like("%" + query + "%")).all()
