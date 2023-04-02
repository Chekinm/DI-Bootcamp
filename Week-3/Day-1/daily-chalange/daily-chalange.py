# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

class Farm:


    def __init__(self,owner_name):
        self.owner_name = owner_name
        self.name = owner_name + '\'s farm'
        self.animals = {}

    def add_animal(self,animal,number=1):
        if animal in self.animals:
            self.animals[animal] += number
        else:
            self.animals[animal] = number
    

    def get_animal_types(self):
        print(sorted(self.animals.keys()))
        return sorted(self.animals.keys())


    def get_info(self):
        animals_list=self.name + '\n\n'
        for animal, num in self.animals.items():
            animal_str =  '\t'+ animal +'\t:\t' + str(num) + '\n'
            animals_list += animal_str
        animals_list += '\n\t\t'+ 'E-I-E-I-O!'
        print(animals_list)
        


    def get_short_info(self):
        anim_plural_names = []
        for anml_type in self.get_animal_types():
            if self.animals[anml_type] > 1 and anml_type != 'sheep':
                anim_plural_names.append (anml_type + 's')
            if self.animals[anml_type] == 1:
                anim_plural_names.append (anml_type)
            if self.animals[anml_type] > 1 and anml_type == 'sheep':
                anim_plural_names.append ('many ' + anml_type)
        if len(anim_plural_names) == 0:
            print(self.name + ' have no animals.')
        if len(anim_plural_names) == 1:
            print(self.name + ' have ' + anim_plural_names[0] + '.')
        if len(anim_plural_names) > 1:
            and_str = [', '.join(anim_plural_names[:-1]), anim_plural_names[-1]]
            print(self.name + ' have ' + ' and '.join(and_str) + '.')



        
            



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep',2)
macdonald.add_animal('goat', 11)
macdonald.add_animal('pig', 11)
print(macdonald.get_info())

macdonald.get_animal_types()
macdonald.get_short_info()



# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!





