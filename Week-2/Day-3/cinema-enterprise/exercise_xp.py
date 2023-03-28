
# abusing DRI principle. Lets use class and functions writen yesterday.
# i organize it a separate module cinema.py 

from cinema import watchers, movie, cinema

family1 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 28}

family_1_watchers = watchers(family1)

my_cinema = cinema({'kid':2,'teen':23, 'adult':100})

my_movie = movie('Kill Bill', True)

my_cinema.print_ticket(family_1_watchers.watchers_list, my_movie)

family2 = {}

family_2_watchers = watchers()
family_2_watchers.read_input()
my_movie2 = movie('Blue moon', True)
my_cinema2 = cinema()
my_cinema2.print_ticket(family_2_watchers.watchers_list, my_movie2)


