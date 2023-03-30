from Cinema import Watchers, Movie, Cinema, Watcher

family1 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 28}

family_1_watchers = Watchers(family1)

Peter = Watcher('peter', 45)
family_1_watchers.append(Peter)
my_cinema = Cinema({'kid':2,'teen':4, 'adult':85})
my_movie = Movie('Kill Bill', False)
my_cinema.print_ticket(family_1_watchers, my_movie)

# family2 = {}

# family_2_watchers = watchers()
# family_2_watchers.read_input()
# my_movie2 = movie('Blue moon', True)
# my_cinema2 = cinema()
# my_cinema2.print_ticket(family_2_watchers.watchers_list, my_movie2)

