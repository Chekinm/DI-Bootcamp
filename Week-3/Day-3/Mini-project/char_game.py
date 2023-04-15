# decorator to print what's happen 
def visualize_action (method):
    def visualised_method(self, *args, **kwargs):
        print('')
        print(type(self).__name__, method.__name__, *(type(arg).__name__ for arg in args))  
        method(self, *args, **kwargs)
        print('State after action:')
        print(self, *args, sep='\n')
    return visualised_method


class Character():

    def __init__(self, life=20, attack=10, is_alive=True):
        self.life = life
        self.attack = attack
        self.is_alive = is_alive

    @visualize_action
    def basic_attack(self, other):
        if self.is_alive:
            other.life -= self.attack
            if other.life < 0:
                other.life = 0
                other.is_alive = False
        else:
            print('The dead don\'t damage!')
    
    def __repr__(self):
        alive_str = 'alive' if self.is_alive else 'dead'
        return f'Class: {type(self).__name__}, life point: {self.life}, attack: {self.attack}, {alive_str}.'
    

class Druid(Character):

    def __init__(self, life=20, attack=10, is_live=True):
        super().__init__(life, attack, is_live)
        print('Hi. new Druid is here!')

    @visualize_action    
    def meditate(self):
        if self.attack > 2:
            self.life += 10
            self.attack -= 2
        else:
            print('No enough selfpower to meditate')
        
    @visualize_action 
    def animal_help(self):
        self.attack += 5

    @visualize_action 
    def fight(self, other):
        if self.is_alive:
            other.life -= (0.75 * self.attack + 0.75 * self.life)
            if other.life < 0:
                other.life = 0
                other.is_alive = False
        else:
            print('The dead don\'t damage!')



class Warrior(Character):


    def __init__(self, life=20, attack=10, is_alive=True):
        super().__init__(life, attack, is_alive)
        print('New Warrior is here. Gonna kill\'em all!')

    @visualize_action 
    def brawl(self, other):
        if self.is_alive:
            other.life -= 2 * self.attack
            if other.life < 0:
                other.life = 0
                other.is_alive = False
            self.life += 0.5 * self.attack
        else:
            print('The dead don\'t damage!')

    @visualize_action      
    def train(self):
        self.attack += 2
        self.life += 2

    @visualize_action 
    def roar(self, other):
        other.attack -= 3
        if other.attack < 0:
            other.attack = 0


class Jedi(Character):


    def __init__(self, life=20, attack=10, is_alive=True):
        super().__init__(life, attack, is_alive)
        print('New Jedi was born. May the Force be with you')
   
    @visualize_action 
    def curse(self, other):
        other.attack -= 2
        if other.attack < 0:
            other.attack = 0

    @visualize_action 
    def summon(self):
        self.attack += 3

    @visualize_action 
    def cast_spell(self, other):
        if self.is_alive:
            # dont' need to check if life is 0 as life can be 0 
            # only after other person attack, and if life is became 0 
            # we set is_Alive to False
            other.life -= self.attack / self.life
            if other.life < 0:
                other.life = 0
                other.is_alive = False
            self.life += 0.5 * self.attack
        else:
            print('The dead don\'t damage!')

    @visualize_action         
    def heal(self,other):
        if self.is_alive and not other.is_alive:
            other.is_alive = True
            other.life = self.life / 2
            self.life /= 2

# create red team
red_druid_one = Druid(30,20)
red_druid_two = Druid(35,20)
red_warior = Warrior()
red_jedi = Jedi(100,100)

# create blue team
blue_druid_one = Druid(30,20)
blue_druid_two = Druid(35,20)
blue_warior = Warrior()
blue_jedi = Jedi(100,100)

# check all druid action
blue_druid_one.meditate()
blue_druid_one.basic_attack(red_druid_one)
blue_druid_one.fight(red_jedi)

# check all warior action
blue_warior.basic_attack(red_warior)
blue_warior.brawl(red_jedi)
blue_warior.train()
blue_warior.roar(red_warior)

# check all jedi action
blue_jedi.basic_attack(red_jedi)
blue_jedi.curse(red_druid_two)
blue_jedi.cast_spell(red_warior)
blue_jedi.summon()
blue_jedi.heal(blue_druid_one)

