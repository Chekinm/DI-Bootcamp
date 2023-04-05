from math import pi
from random import randint

class Circle():
        
    def __init__(self, size: float, size_type='radius'):
        if size_type == 'radius':
            self.diameter = size * 2
            self.radius = size
        elif size_type == 'diameter':
            self.diameter = size
            self.radius = size /2

    @property
    def area (self):
        return self.radius ** 2 * pi
    
    @property
    def perimetr (self):
        return self.radius * 2 * pi

    def __str__(self):
        return f'Circle with radius {self.radius}.'

    def __add__(self, other):
        return Circle (self.radius + other.radius)
    
    def __iadd__(self, other):
        self.radius += other.radius
        self.diameter = self.radius * 2
        return self

    def __eq__(self, other) -> bool:
        return True if self.radius == other.radius else False
    
    def __lt__(self, other):
        return True if self.radius < other.radius else False
        
    def __le__(self, other):
        return True if self.radius <= other.radius else False
        
    def __gt__(self, other):
        return True if self.radius > other.radius else False
        
    def __ge__(self, other):
        return True if self.radius >= other.radius else False
    
    def __ne__(self, other):
        return True if self.radius != other.radius else False
        
n = 20        
        
list_of_circle1 = [0]* n 
list_of_circle2 = [0]* n
list_of_circle_sum = [0] * n
big_circle = Circle(0)

for i in range(n):
    list_of_circle1[i] = Circle(randint(1,100))
    list_of_circle2[i] = Circle(randint(1,100), 'diameter')
    list_of_circle_sum[i] = list_of_circle1[i] + list_of_circle2[i]
    print(list_of_circle_sum[i])
    big_circle += list_of_circle1[i]
    big_circle += list_of_circle2[i] 
    print(big_circle)  

list_of_circle_sum.sort()

for i in range(n):
    print(list_of_circle_sum[i].radius)

print('\n')
print(big_circle)


