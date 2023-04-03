from XPexercise import Dog
from random import choice

DOG_TRICKS = [
    ' does a barrel roll.',
    ' stands on his back legs.',
    ' shakes your hand.',
    ' dog_name plays dead.',
    ]

class PetDog(Dog):
    #   an attribute called trained to the __init__ method, 
    #  this attribute is a boolean
    #  and the value should be False by default.
    def __init__(self, name, age, weight, is_trained=False):
        super().__init__(name, age, weight)
        self.is_trained = is_trained

    # Add the following methods:
    # train: prints the output of bark and switches the 
    # trained boolean to True
    def train(self):
        self.bark()
        self.is_trained = True
        
    def play(*args):
        dog_names = ', '.join(dg.name for dg in args)
        return(f'{dog_names} all play toghether')
    
    def do_a_trick(self):
        if self.is_trained:
            print(self.name + choice(DOG_TRICKS))
        else:
            print(f'{self.name} has not trained yet.')

    
vasya_the_dog = PetDog('Vasya', 20, 30)
york_is_not_a_dog_actually = PetDog('Glasha',1,1)
dog1 = Dog('Sharik', 20, 10) #100/200
dog2 = Dog('Bobby', 40, 15) #225/400
dog3 = Dog('Kleo', 7, 6)   #36/70


print(vasya_the_dog.play(dog1,dog2))
vasya_the_dog.train()

vasya_the_dog.do_a_trick()
york_is_not_a_dog_actually.do_a_trick()

