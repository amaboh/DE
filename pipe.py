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


genres_list = df['genres'].tolist()


flat_list = [item for sublist in genres_list for item in sublist]

result = []

for l in genres_list:
    r = []
    for d in l:
        r.append(d['name'])
    result.append(r)
df = df.assign(genres_all= result)

df_genres = pd.DataFrame.from_records(flat_list).drop_duplicates()


df_genres_columns = df_genres['name'].to_list()
df_columns.extend(df_genres_columns)

s = df['genres_all'].explode()
df = df.join(pd.crosstab(s.index, s))


df['release_date'] = pd.to_datetime(df['release_date'])
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year
df['day_of_work'] = df['release_date'].dt.day_name()
df_time_columns = ['id', 'release_date', 'day', 'month', 'year', 'day_of_work']

df[df_time_columns]