import pandas as pd
import requests
import config

API_KEY = config.api_key


# url = url = 'https://api.themoviedb.org/3/movie/550?api_key={API_KEY}'.format(movie_id, API_KEY)
response_list = []

for movie_id in range(550,556):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, API_KEY)
    r = requests.get(url)
    response_list.append(r.json())


df = pd.DataFrame.from_dict(response_list)

df_columns = ['budget', 'genres', 'id', 'imdb_id', 'orginal_title', 'release_date', 'revenue', 'runtime']




