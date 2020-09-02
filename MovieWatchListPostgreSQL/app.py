import datetime
import moviesdatabase

# Here is menu that is displayed so user knows what to input
menu = """Please select what you want to do:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add new user.
7) Search for a movie.
8) Exit.

Your selection: """
# Here is welcome message
welcome = "Welcome to movie watchlist application!\n"

print(welcome)
moviesdatabase.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY)")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    moviesdatabase.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --\n")
    for _id, title, release_date in movies:  # I am using _id so build in function "id" is not overwritten
        movie_date = datetime.datetime.fromtimestamp(release_date)
        normal_date = movie_date.strftime("%d %b %Y")
        print(f'{_id}: {title} (on {normal_date})')
    print("----", "\n")


def prompt_watch_movie():
    username = input("Enter your username: ")
    movie_id = input("Movie ID: ")
    moviesdatabase.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    moviesdatabase.add_user(username)


def prompt_view_watched_movies():
    username = input("Username: ")
    movies = moviesdatabase.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username} watched movies: ", movies)
    else:
        print("You haven't watched any movie yet.")


def prompt_search_movies():
    search_term = input("Enter whole or partial movie title: ")
    movies = moviesdatabase.search_movies(search_term)
    if movies:
        print_movie_list("Movies that've been found:", movies)
    else:
        print("No movies were found for that searched term")


# Main loop that prompts input from user and takes corresponding action
while (user_input := input(menu)) != '8':
    if user_input == '1':
        prompt_add_movie()
    elif user_input == '2':
        movies = moviesdatabase.get_movies(True)  # True if upcoming
        print_movie_list("Upcoming", movies)
    elif user_input == '3':
        movies = moviesdatabase.get_movies(False)  # False if all movies
        print_movie_list("All", movies)
    elif user_input == '4':
        prompt_watch_movie()
    elif user_input == '5':
        prompt_view_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input! Please enter number between (1-8): ")
