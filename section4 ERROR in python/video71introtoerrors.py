def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')
    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movies['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")
    
