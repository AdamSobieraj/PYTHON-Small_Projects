import random

from mod_5.movi.Movie import Movie
from mod_5.movi.Series import Series


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_movies(self):
        return sorted([item for item in self.items if isinstance(item, Movie)])

    def get_series(self):
        return sorted([item for item in self.items if isinstance(item, Series)])

    def search(self, title):
        return next((item for item in self.items if item.title.lower() == title.lower()), None)

    def generate_views(self):
        return random.randint(1, 100)

    def run_generate_views(self, times=10):
        for i in range(times):
            item = random.choice(self.items)
            item.views += self.generate_views()

    def top_titles(self, quantity=5, content_type=None):
        if content_type == "movies":
            items = self.get_movies()
        elif content_type == "series":
            items = self.get_series()
        else:
            items = self.items
        return sorted(items, key=lambda x: x.views, reverse=True)[:quantity]

