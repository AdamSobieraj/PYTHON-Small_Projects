from mod_5.movi.Movie import Movie

class Series(Movie):
    def __init__(self, title, year, genre, episode_number, season_number):
        super().__init__(title, year, genre)
        self.episode_number = episode_number
        self.season_number = season_number
        self.views = 0

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

    def get_info(self):
        return f"{self.__str__()}"

    def __lt__(self, other):
        return self.views < other.views

    def __le__(self, other):
        return self.views <= other.views

    def __gt__(self, other):
        return self.views > other.views

    def __ge__(self, other):
        return self.views >= other.views

    @property
    def full_title(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
