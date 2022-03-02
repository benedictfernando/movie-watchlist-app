
import database
import helper


menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


while (user_input := input(menu)) != "6":
    if user_input == "1":
        helper.prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        helper.print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        helper.print_movie_list("All", movies)
    elif user_input == "4":
        helper.prompt_watch_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        helper.print_movie_list("Watched", movies)
    else:
        print("Invalid input, please try again!")
