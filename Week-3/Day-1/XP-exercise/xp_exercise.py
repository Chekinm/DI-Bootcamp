# 🌟 Exercise 1: Cats
# Instructions
# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

def oldest_cat (*cats: Cat) -> None:
    oldest_cat = max(cats, key=lambda x: x.age)
    print(f'Oldest cat here - {oldest_cat.name}')


cat_one = Cat('Boris', 13)
cat_two = Cat('Fedya', 12)
cat_three = Cat('Mike', 47)

oldest_cat(cat_one, cat_two, cat_three)


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
class Dog():

    def __init__(self, name, heigth):
# In this class, create an __init__ method that takes two 
# parameters : name and height. This function instantiates 
# two attributes, which values are the parameters.
        self.name = name
        self.heigth = heigth
# Create a method called bark that prints the following string 
# “<dog_name> goes woof!”.
    def bark (self):
        print(f'{self.name} goes woof!')
# Create a method called jump that prints the following string 
# “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump (self):
        print(f'{self.name} jumps {self.heigth * 2} cm high')
# Outside of the class, create an object called davids_dog.
#  His dog’s name is “Rex” and his height is 50cm.

davids_dog = Dog('Rex',50)


# Print the details of his dog (ie. name and height) and 
# call the methods bark and jump.

print(f'{davids_dog.name} is {davids_dog.heigth} high.')
davids_dog.jump()
davids_dog.bark()
# Create an object called sarahs_dog. Her dog’s name is 
# “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call 
# the methods bark and jump.


saras_dog = Dog('Teacup',20)
print(f'{saras_dog.name} is {saras_dog.heigth} high.')
saras_dog.jump()
saras_dog.bark()

# Create an if statement outside of the class to check which 
# dog is bigger. Print the name of the bigger dog.

if saras_dog.heigth > davids_dog.heigth:
    print(f'{saras_dog.name} is higher than {davids_dog.name} by {saras_dog.heigth - davids_dog.heigth} cm')
elif saras_dog.heigth < davids_dog.heigth:
    print(f'{davids_dog.name} is higher than {saras_dog.name} by {davids_dog.heigth - saras_dog.heigth} cm')
else:
    print(f'{davids_dog.name} is same hight as {saras_dog.name}. They are {saras_dog.heigth} cm high.')

# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics   
    
    def sing_me_a_song(self):
        print(*self.lyrics, sep='\n')


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.

class Zoo():
   

# In this class create a method __init__ that takes one parameter:
#  zoo_name.

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

# It instantiates two attributes: animals (an empty list) 
# and name (name of the zoo).
# Create a method called add_animal that takes one parameter 
# new_animal. This method adds the new_animal to the animals 
# list as long as it isn’t already in the list.
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)



# Create a method called get_animals that prints all the 
# animals of the zoo.

    def get_animals(self):
        print(*self.animals, sep='\n')

# Create a method called sell_animal that takes one parameter 
# animal_sold. This method removes the animal from the list 
# and of course the animal needs to exist in the list.

    def sell_animal (self, sold_animal):
        try:
            self.animals.remove(sold_animal)
        except:
            print(f'we do not have {sold_animal} in our zoo.')
# Create a method called sort_animals that sorts the animals 
# alphabetically and groups them together based on their 
# first letter.
# Example


    def sort_animals(self):
        dict_animals1 = {}
        for animal in self.animals:
            if animal[0] not in dict_animals1:
                dict_animals1[animal[0]] = [animal]
            else:
                dict_animals1[animal[0]].append(animal)
        i = 1
        self.dict_animals = {}
        for key in sorted (dict_animals1.keys()):
            self.dict_animals[i] = dict_animals1[key]
            i += 1   
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method called get_groups that prints the animal/animals inside each group.
    def get_groups(self):
        self.sort_animals()
        for key in self.dict_animals:
            print(self.dict_animals[key])
# Create an object called ramat_gan_safari and call all the methods.

ramat_gan_safari = Zoo('Ramatgan Safari')

list_animal = ['Cougar', 'Eel', 'Ape', 'Baboon', 'Bear', 'Cat',  'Emu','Lyon']

for anim in list_animal:
    ramat_gan_safari.add_animal(anim)

ramat_gan_safari.get_animals()
# try do sell anumal which doesn't exist
ramat_gan_safari.sell_animal('Mouse')
# sell existing animal
ramat_gan_safari.sell_animal('Lyon')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()


# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


