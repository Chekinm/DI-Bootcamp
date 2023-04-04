# Exercise 1 : Family
from functools import reduce
from operator import and_

class Family():
        
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **child_details):
        
        self.members.append({key: value for key, value in child_details.items()})
        print('Dear {}s. Congtatulations with a new family memeber {}.'.format(self.last_name, self.members[-1]['name']))

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return True  if member['age'] >= 18 else False
        raise ValueError (f'{name} is not found in family.')

    def family_presentation(self):
        print(f'Our family nams is {self.last_name}.')
        print('And this is our family memeber:')
        for member in self.members:
            print(member['name'], sep = '\n')
        
# Exercise 2 : TheIncredibles Family

class TheIncredibles(Family):

    def __init__(self, last_name, members):
        super().__init__(last_name, members)
        is_incridable = reduce(lambda x, y: x & y,  [('power' in member) for member in members], True)
        if is_incridable:
            self.is_incridable = True
        else:
            raise TypeError('You are trying to initilse TheIncridable type family with normal family input')

    def use_power(self, name):
        if self.is_18(name):
            for member in self.members:
                if member['name'] == name:
                    power = member['power']
                    print(f'{name} can {power}')

        else:
            raise TypeError (f'Family memeber {name} is not old enough to use power')

    
    def born(self, **inc_child_details):
        if 'power' in inc_child_details:
            super().born(**inc_child_details)
        else:
            raise TypeError('you are trying to add normal mamber to incridable family')

    def family_presentation(self):
        super().family_presentation()
        print('Our family is incridable')
        for member in self.members:
            name =  member['name']
            inc_name =  member['incredible_name']
            power = member['power']
            gen = 'he' if member['gender'] == 'Male' else 'she'
            print(f'{name} has incridable name {inc_name}, and {gen} has a special power, {gen} can {power}.')


members= [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False},
]

johnson = Family('Johnson', members)
johnson.family_presentation()
johnson.born(name='Vasya',age = 0,gender='Male',is_child=True)
johnson.family_presentation()

print('\n\n')


members_incridable = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
smith = TheIncredibles('Smith', members_incridable)
smith.family_presentation()
smith.born(name='SuperVasya',age = 0,gender='Male',is_child=True, power ='unknown power', incredible_name = 'SuperChild')
smith.family_presentation()
 