import datetime
import moviesdatabase

# Here is menu that is displayed so user knows what to input
menu = """Please select what you want to do:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit program.

Your selection: """
# Here is welcome message
welcome = "Welcome to movie watchlist application!"

print(welcome)
moviesdatabase.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY)")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    moviesdatabase.add_movie(title, timestamp)


def print_movie_list(movies):
    print("---- Upcoming movies ----\n")
    for movie in movies:
        print(f'{movie[0]} (on {movie[1]})')
    print("---> \n")


# Main loop that prompts input from user and takes corresponding action
while (user_input := input(menu)) != '6':
    if user_input == '1':
        prompt_add_movie()
    elif user_input == '2':
        movies = moviesdatabase.get_movies(True) # True because we want upcoming movies (see get_movies func)
        print_movie_list(movies)
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    else:
        print("Invalid input! Please enter number between (1-6): ")
