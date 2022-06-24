from presenter.models.movie import Movie
from presenter.models.actor import Actor
import ipdb


class Search:
    def search(self, query=""):
        results = dict()
        for model, attribute in self.searchable_models():
            results[model.__tablename__] = self._model_search(model, attribute, query)
        return results

    def searchable_models(self):
        return [(Movie, "title"), (Actor, "name")]

    def _model_search(self, model, attribute, query):
        return model.query.filter(getattr(model, attribute).like("%" + query + "%")).all()

    def index():
        search_string = request.args.get("q")
        if search_string == "":
            return render_template("/homepage/index.html")
        else:
            search_result = Movie.query.filter(Movie.title.like("%" + search_string + "%")).all()
            print(search_result)
            per_page = request.args.get("items", 5, type=int)
            current_page = request.args.get("page", 1, type=int)
            movie_count = len(search_result)
            start = per_page * (current_page - 1)
            end = min(start + per_page, movie_count)
            movies = search_result[start:end]
            mess = ""
            if len(search_result) == 0:
                mess = f"Nothing was found for {search_string} "
            elif len(movies) == 0:
                mess = "No more items"
        return render_template(
            "/search.html",
            movies=movies,
            query=search_string,
            current_page=current_page,
            items_per_page=per_page,
            mess=mess,
        )
