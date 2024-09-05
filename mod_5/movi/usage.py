import random

from mod_5.movi.Library import Library
from mod_5.movi.Movie import Movie
from mod_5.movi.Series import Series

library = Library()

# Dodaj filmy i seriale do biblioteki
library.add_item(Movie("Pulp Fiction", 1994, "Crime"))
library.add_item(Series("The Simpsons", 1989, "Animated", 5, 1))
library.add_item(Movie("Inception", 2010, "Sci-Fi"))
library.add_item(Series("Breaking Bad", 2008, "Drama", 1, 1))

# Przykład użycia funkcji
print(library.top_titles(content_type="movies"))

# Uruchom generowanie widoków 10 razy
library.run_generate_views()

# Wyświetl informacje o filmie
pulp_fiction = library.search("Pulp Fiction")
print(pulp_fiction.get_info())

# Wyświetl informacje o serialu
the_simpsons = library.search("The Simpsons")
print(the_simpsons.get_info())

# Wyświetl top 3 najpopularniejszych tytułów
top_items = library.top_titles(quantity=3)
for item in top_items:
    print(item.get_info(), f"Views: {item.views}")