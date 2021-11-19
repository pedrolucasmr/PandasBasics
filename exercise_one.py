#Using TMDB movies as dataset, get mean of vote average of each original language.
import pandas as pd
import seaborn as sns


tmdb_movies_path = "data/tmdb_5000_movies.csv"
tmdb = pd.read_csv(tmdb_movies_path)

rates_means = {}
languages = tmdb.original_language.unique()
print(languages)

for language in languages:
    rates_means[language] = tmdb.query("original_language == @language").vote_average.mean()

print(rates_means)


