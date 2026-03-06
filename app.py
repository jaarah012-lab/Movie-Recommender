import pandas as pd

movies = pd.read_csv("movies.csv")

movies['Title'] = movies['Title'].str.lower()
movies['Genre'] = movies['Genre'].str.lower()

print("Available genres:")
print(movies['Genre'].unique())
genre_input = input("Enter movie genre: ").lower()
num_movies = int(input("How many movies do you want? "))


filtered_movies = movies[movies['Genre'].str.contains(genre_input)]
top_movies = filtered_movies.head(num_movies)

if len(top_movies) == 0:
    print("No movies found for this genre.")
else:
    print(f"\nTop {num_movies} movies in {genre_input}:\n")
    for i in top_movies['Title']:
        print(i)
        