import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#movielens
#movies_path = "data/movies.csv"
#ratings_path = "data/ratings.csv"

#movies_dataset = pd.read_csv(movies_path)
#ratings_dataset = pd.read_csv(ratings_path)

#rating_series = ratings_dataset["rating"]
#users_rating_mean = ratings_dataset.groupby("userId").rating.mean()
#movies_rating_mean = ratings_dataset.groupby("movieId").rating.mean()

#movies_plot = sns.histplot(data=movies_rating_mean, kde=True)
#users_plot = sns.histplot(data=users_rating_mean, kde=True)
#plt.show()


#print(movies_dataset.head())
#print(ratings_dataset.head())
#print(rating_series.head())
#print(rating_series.mean())
#print(users_rating_mean)
#print(movies_rating_mean)



#tmdb

tmdb_movies_path = "data/tmdb_5000_movies.csv"
tmdb_credits_path = "data/tmdb_5000_credits.csv"

tmdb_movies_dataset = pd.read_csv(tmdb_movies_path)
tmdb_credits_dataset = pd.read_csv(tmdb_credits_path)
#print(tmdb_movies_dataset.head())
#print(tmdb_movies_dataset.original_language.unique())
#print(tmdb_movies_dataset.original_language.value_counts())



ja_movies = tmdb_movies_dataset.loc[tmdb_movies_dataset["original_language"] == "ja"]
print(ja_movies.title)

languages_count = tmdb_movies_dataset.original_language.value_counts()
ja_count = languages_count.loc["ja"]
print(ja_count)
