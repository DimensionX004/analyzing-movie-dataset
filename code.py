# --------------
from csv import reader

def explore_data(dataset, start, end, rows_and_columns=False):
    movDetails = []
    for i in range(start, end):
        movDetails.append(movies[i])
    #print(movDetails)

def duplicate_and_unique_movies(dataset, index_):
    chklist = [] 
    duplicate = []
    for i in range(0,4802):
        if dataset[i][index_] not in chklist:
            chklist.append(dataset[i][index_])
        else:
            duplicate.append(dataset[i][index_])
    #print("Duplicate movie(s):",duplicate)
    return duplicate

def movies_lang(dataset, index_, lang_):
    movies_ = []
    for i in range(4802):
        if(dataset[i][index_]=='en'):
            movies_.append(dataset[i][index_])    
    return movies_

def rate_bucket(dataset, rate_low, rate_high):
    rated_movies = []
    for i in range(0,4802):
        if float(dataset[i][11])>=8 and float(dataset[i][11])<=10 and (dataset[i][3])=='en':
            rated_movies.append(dataset[i][13])
        else:
            pass
    return rated_movies

# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]

# Subset the movies dataset such that the header is removed from the list and store it back in movies
temp = []
for i in movies:
    if i != movies[0]:
        temp.append(i)
movies = temp

# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
movies.pop(4553)

# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies_header, 0, 5)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies, 13)

# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max = {}
for i in range(4802):
    reviews_max[movies[i][13]] = movies[i][12] 

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
dups = duplicate_and_unique_movies(movies, 13)
for i in dups:
    movies_clean.append(reviews_max[i])

# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en = movies_lang(movies,13,'en')
#print(movies_en)

# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies,8,10)
#print(high_rated_movies)


