import csv

from covid.domain.model import Movie
from covid.domain.model import Actor
from covid.domain.model import Genre
from covid.domain.model import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = set()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                m = Movie(title, release_year)
                self.__dataset_of_movies.add(m)
                d = Director(row['Director'])
                self.__dataset_of_directors.add(d)
                actor_list = (row['Actors']).split(",")
                for actor in actor_list:
                    a = Actor(actor)
                    self.__dataset_of_actors.add(a)
                genre_list = (row['Genre']).split(",")
                for genre in genre_list:
                    g = Genre(genre)
                    self.__dataset_of_genres
                index += 1

