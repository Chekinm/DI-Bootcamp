# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
from math import pi
class Circule():
    

        def __init__(self, radius=1.0):
            self.radius = radius
            
        def perimeter (self):
            perimeter = 2 * pi * self.radius
            return perimeter
        
        def area(self):
            area = pi * self.radius ** 2
            return area
        
        def definition(self):
             print('A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the centre).')


a = Circule(10)
print(a.area(), a.perimeter())


# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
from random import randint

class My_list():
     
    def __init__(self, letter_list):
        self.letter_list = letter_list

    def myreverse(self):
        return [*reversed(self.letter_list)]

    def mysort(self):
        return sorted(self.letter_list)
    
    def random_list(self):
         return [randint(1,len(self.letter_list)) for _ in range(len(self.letter_list))]

a = My_list(['b','a','d', 'c',])

print(a.random_list())
print(a.myreverse())
print(a.mysort())