import requests
import json

class URLMaker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_movie_url(self, category='movie', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'

        return url

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None

    def get_genre_url(self):
        url = f'{URLMaker.url}/genre/movie/list?api_key={self.key}&language=ko-KR'
        return url

TMDB_KEY = '05c7e80b2d8878d5eaf42501024385e9'
url = URLMaker(TMDB_KEY)

def create_genre_data():
    genre_url = url.get_genre_url()
    raw_data = requests.get(genre_url)
    json_data = raw_data.json()
    genres = json_data.get('genres')

    genre_data = []

    for genre in genres:
        tmp = {
            'model': 'movies.genre',
            'pk': genre['id'],
            'fields': {
                'genre_id': genre['id'],
                'name': genre['name']
            }
        }
        genre_data.append(tmp)

    with open('genres.json', 'w', encoding="utf8") as f:
        json.dump(genre_data, f, indent=2, ensure_ascii = False)

def create_movie_data():
    with open('genres.json', 'r+', encoding="utf8") as f:
        movie_data = json.load(f)

    for page in range(61, 91):
        raw_data = requests.get(url.get_movie_url(page=page))
        json_data = raw_data.json()
        movies = json_data.get('results')

        # print(movies)

        for movie in movies:
            if movie.get('release_date') == "" or movie.get('poster_path') == "":
                continue

            # movie.pop('adult')
            # movie.pop('original_language')
            # movie.pop('original_title')
            # movie.pop('popularity')
            movie.pop('backdrop_path')
            movie.pop('video')
            # movie.pop('vote_count')
            movie['movie_id'] = movie.pop('id')
            # movie['like_users'] = []
            tmp = {
                'model': 'movies.movie',
                'pk': 1,
                'fields': movie,
            }
            movie_data.append(tmp)
            print(tmp)

    with open('movies.json', 'w', encoding="utf8") as f:
        json.dump(movie_data, f, indent=2, ensure_ascii = False)

create_genre_data()
create_movie_data()

