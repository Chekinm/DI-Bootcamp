# cinema library
# implemented classes:


class watcher():
    """ hold information about person, constructor calculate
        age price group according to bondles, witch can be ajusted
        there is also restricted attributes for adults restritions"""
    def __init__(self, name, age, restricted="False"):
        kid_age = 3
        teen_age = 12
        adult_age = 21
        self.name = name
        self.age = age
        self.price_group = '' 
        self.restricted = (True if age < adult_age else False) 
        # I change this from original to be logical -> just less than 21
        if self.age < kid_age:
            self.price_group = 'kid'
        elif self.age < teen_age:
            self.price_group = 'teen'
        else:
            self.price_group = 'adult'

class watchers():
    """holds groups of watchers as list of class wather object 
        there is two method to fill the group
        - read from dict ({name:age})
        - read from input
    """
    def __init__(self, watchers_dict=None):
        if watchers_dict == None:
            self.watchers_list = []
        else:
            self.watchers_list = []
            for name, age in watchers_dict.items():
                self.watchers_list.append(watcher(name,age))
    
    def read_dict(self, dict_of_watchers):
        for name, age in dict_of_watchers.items():
            self.watchers_list.append(watcher(name,age))

    def clear(self):
        self.watchers_list.clear()
            
    def read_input(self):
        print('Enter number of persons in the group:')
        num_of_person = int(input())
        self.watchers_list = []
        for i in range(num_of_person):
            print(f'Enter the name of the person number {i+1}:')
            name_i = input()
            print(f'Enter the age of the person number {i+1}:')
            age_i = int(input())
            self.watchers_list.append(watcher(name_i, age_i))
        print(self.watchers_list[0].name)

        
class movie():
    """
    bocie class to hold name and age restriction
    """
    def __init__(self, name, is_adult=False):
        self.name = name
        self.is_adult = is_adult
    

class cinema():
    """
    cinema class holds the price list and has a method to issue 
      a ticket to a group of wathers, depends on movie and ages of the group
    """


    def __init__(self, price_list=None):
        if price_list == None:
            self.price_list = {
                'kid': 0,
                'teen': 10,
                'adult': 15,
            }
        else:
            self.price_list = price_list
            

    def print_ticket(self, watchers_list, movie):
        """ Gets wathers list (as watchers) and movie as movie and 
        print a ticket for wathers list
        """
        self.total = 0
        forbiden_list = []
        allowed_list = []
        print('-------------------------------------') 
        for person in watchers_list:
            if movie.is_adult and person.restricted:
                forbiden_list.append(person.name + ' - ' + str(person.age) + ' years')
                continue
            person_price = self.price_list[person.price_group]
            self.total += person_price
            allowed_per_str = f'{person.name} \t  --- {person_price} shekels'
            allowed_list.append(allowed_per_str)
            
        if forbiden_list:
            print(f'Unfortunatley this person is not allowed to watch the {movie.name}:')
            print(*forbiden_list, sep='\n')
            if allowed_list:
                print('This is a check for others:')
        else:
            if allowed_list:
                print("Here is you check:")
                    
        if allowed_list:
            print(f'You bought a group ticket to {movie.name}:')
            print(*allowed_list, sep='\n')
            print(f'total price is   {self.total}  shekels')
        
        print('-------------------------------------') 


