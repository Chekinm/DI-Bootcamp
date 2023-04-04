# import sys
# import traceback

# class Door():

#     def __init__(self, name, is_open=True):
#         self.name = name
#         self.is_open = is_open

#     def open_door(self):
#         self.is_open = True


#     def close_door(self):
#         self.is_open = False

# class BlockDoor(Door):

#     def __init__(self, name):
#         super().__init__(name, is_open=False)
    
#     def open_door(self):
#         raise TypeError (f'The door - {self.name} is blocked')
#     def close_door(self):
#         raise TypeError  (f'The door - {self.name} is blocked')


# a = Door('a',True)
# b = BlockDoor('b')
# try:
#     b.open_door()
# except TypeError:
    
#     print('I can pritn stack exeption')
#     traceback.print_exc()
#     print('it pritnts by itself')



# finally:
#     print('WE are here')

def a (**kwargs):
    print(kwargs)

a = a(a=2, b=3)    


