class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    


### Ex 2

class Dog():

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark (self):
        return f'{self.name} is barking'
    
    def run_speed(self): 
        # calcualte and return running speed
        return self.weight / (self.age * 10) 
    


    def fight (self, sparring_p):
        power_s = self.weight * self.run_speed() 
        power_sp_p = sparring_p.weight * sparring_p.run_speed() 
        print(power_s,power_sp_p)
        if power_s == power_sp_p:
            winner = 'nobody'
        elif power_s > power_sp_p:
            winner = self.name
        else:
            winner = sparring_p.name

        return (f'{winner} won the fight.')

if __name__=='__main__':

    cat1 = Bengal('Murka',4)
    cat2 = Chartreux('Jurka',5)
    cat3 = Siamese('Palaphel',3)
    list_all_cat = [cat1, cat2, cat3]

    sara_pets = Pets(list_all_cat)

    sara_pets.walk()
    dog1 = Dog('Sharik', 20, 10) #100/200
    dog2 = Dog('Bobby', 40, 15) #225/400
    dog3 = Dog('Kleo', 7, 6)   #36/70
    print(dog1.fight(dog2))
    print(dog2.fight(dog3))
    print(dog3.fight(dog1))