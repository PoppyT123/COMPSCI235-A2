from datetime import date, datetime
from typing import List, Iterable


class User:
    def __init__(
            self, username: str, password: str
    ):
        self._username: str = username
        self._password: str = password
        self._comments: List[Comment] = list()

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def comments(self) -> Iterable['Comment']:
        return iter(self._comments)

    def add_comment(self, comment: 'Comment'):
        self._comments.append(comment)

    def __repr__(self) -> str:
        return f'<User {self._username} {self._password}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return other._username == self._username


class Comment:
    def __init__(
            self, user: User, article: 'Article', comment: str, timestamp: datetime
    ):
        self._user: User = user
        self._article: Article = article
        self._comment: Comment = comment
        self._timestamp: datetime = timestamp

    @property
    def user(self) -> User:
        return self._user

    @property
    def article(self) -> 'Article':
        return self._article

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def __eq__(self, other):
        if not isinstance(other, Comment):
            return False
        return other._user == self._user and other._article == self._article and other._comment == self._comment and other._timestamp == self._timestamp


class Article:
    def __init__(self, date: int, title: str, first_para: str, hyperlink: str, image_hyperlink: str, id: int = None, director: str = None, actors = None, runtime: int = None, rating: float = None):
        self._id: int = id
        self._date: int = date
        self._title: str = title
        self._first_para: str = first_para
        self._hyperlink: str = hyperlink
        self._image_hyperlink: str = image_hyperlink
        self._comments: List[Comment] = list()
        self._tags: List[Tag] = list()
        self._director: str = director
        self._actors: List[str] = actors
        self._runtime: int = runtime
        self._rating: float = rating

    @property
    def id(self) -> int:
        return self._id

    @property
    def date(self) -> int:
        return self._date

    @property
    def title(self) -> str:
        return self._title

    @property
    def first_para(self) -> str:
        return self._first_para

    @property
    def hyperlink(self) -> str:
        return self._hyperlink

    @property
    def image_hyperlink(self) -> str:
        return self._image_hyperlink

    @property
    def comments(self) -> Iterable[Comment]:
        return iter(self._comments)

    @property
    def director(self) -> str:
        return self._director

    @property
    def actors(self) -> Iterable[str]:
        return iter(self._actors)

    @property
    def runtime(self) -> int:
        return self._runtime

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def number_of_comments(self) -> int:
        return len(self._comments)

    @property
    def number_of_tags(self) -> int:
        return len(self._tags)

    @property
    def tags(self) -> Iterable['Tag']:
        return iter(self._tags)

    def is_tagged_by(self, tag: 'Tag'):
        return tag in self._tags

    def is_tagged(self) -> bool:
        return len(self._tags) > 0

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def add_tag(self, tag: 'Tag'):
        self._tags.append(tag)

    def __repr__(self):
        return f'<Article {self._date} {self._title}>'

    def __eq__(self, other):
        if not isinstance(other, Article):
            return False
        return (
                other._date == self._date and
                other._title == self._title and
                other._first_para == self._first_para and
                other._hyperlink == self._hyperlink and
                other._image_hyperlink == self._image_hyperlink
        )

    def __lt__(self, other):
        return self._date < other._date


class Tag:
    def __init__(
            self, tag_name: str
    ):
        self._tag_name: str = tag_name
        self._tagged_articles: List[Article] = list()

    @property
    def tag_name(self) -> str:
        return self._tag_name

    @property
    def tagged_articles(self) -> Iterable[Article]:
        return iter(self._tagged_articles)

    @property
    def number_of_tagged_articles(self) -> int:
        return len(self._tagged_articles)

    def is_applied_to(self, article: Article) -> bool:
        return article in self._tagged_articles

    def add_article(self, article: Article):
        self._tagged_articles.append(article)

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return False
        return other._tag_name == self._tag_name


class ModelException(Exception):
    pass


def make_comment(comment_text: str, user: User, article: Article, timestamp: datetime = datetime.today()):
    comment = Comment(user, article, comment_text, timestamp)
    user.add_comment(comment)
    article.add_comment(comment)

    return comment


def make_tag_association(article: Article, tag: Tag):
    if tag.is_applied_to(article):
        raise ModelException(f'Tag {tag.tag_name} already applied to Article "{article.title}"')

    article.add_tag(tag)
    tag.add_article(article)

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