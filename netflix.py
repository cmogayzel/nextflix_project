import pandas as pd 
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("dataset/netflix_data.csv", index_col= 0)



netflix_subset = netflix_df[netflix_df["type"] == 'Movie']

netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]

short_movies = netflix_movies[netflix_movies.duration < 60]

# creating a color scheme list
colors = []


for lab, rows in netflix_movies.iterrows(): 
    if rows['genre'] == "Children":
        colors.append('red')
    elif rows['genre'] == "Documentaries":
        colors.append('blue')
    elif rows['genre'] == "Stand-Up":
        colors.append('green')
    else:
        colors.append('black')

# Inspecting the first 10 values only from the list.
colors[:10]

fig = plt.figure(figsize=(12,8))


plt.scatter(netflix_movies.release_year,netflix_movies.duration, c=colors)


# Create a title and axis labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")



# show the plot
plt.show()

#Movie Question
answer = "no"

