class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_info(self):
        return f"{self.__str__()}"

    # porównywania obiektów Movie
    def __lt__(self, other):
        return self.views < other.views

    def __le__(self, other):
        return self.views <= other.views

    def __gt__(self, other):
        return self.views > other.views

    def __ge__(self, other):
        return self.views >= other.views
