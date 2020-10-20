class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if isinstance(other, Director) and self.__director_full_name == other.__director_full_name:
            return True
        return False

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if isinstance(other, Genre) and self.__genre_name == other.__genre_name:
            return True
        return False

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__colleague_set = set()

    @property
    def actor_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if isinstance(other, Actor) and self.__actor_full_name == other.__actor_full_name:
            return True
        return False

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if isinstance(colleague, Actor):
            self.__colleague_set.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if isinstance(colleague, Actor):
            return colleague in self.__colleague_set


class Movie:
    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year < 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

        self.__description = None
        self.__director = None
        self.__runtime_minutes = None
        self.__actors = []
        self.__genres = []


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year):
        if release_year < 1900 or type(release_year) != int:
            self.__release_year = None
        else:
            self.__release_year = release_year

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) == str:
            self.__description = description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        if isinstance(director, Director):
            self.__director = director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if type(time) == int and time > 0:
            self.__runtime_minutes = time
        else:
            raise ValueError

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if isinstance(other, Movie) and (self.__title, self.__release_year) == (other.__title, other.__release_year):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Movie):
            if self.__title != other.__title:
                return self.__title < other.__title
            else:
                return self.__release_year < other.__release_year

    def __hash__(self):
        movie_year = self.__title + str(self.__release_year)
        return hash(movie_year)

    def add_actor(self, actor):
        if isinstance(actor, Actor) and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors and isinstance(actor, Actor):
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre) and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres and isinstance(genre, Genre):
            self.__genres.remove(genre)
