class MenuManager():


    def __init__(self, menu=None) -> None:
        if menu == None or menu == []:
            self.menu =[]
            self.menu_names = []
        else:
            self.menu = menu
            self.menu_names = [meal['name'] for meal in menu]

    def add_item(self, name, price, spice, gluten):
        """ This method will add new dishes to the menu."""
        if name not in self.menu_names:
            self.menu_names.append(name)
            self.menu.append({'name':name,
                            'price':price,
                            'spice_lavel': spice,
                            'glute_index': gluten})
        else:
            print(f'Meal {name} already exists in the menu.')
        
    def update_item(self, name, price, spice, gluten):
        """ This method checks whether a dish is in the menu, 
        if the dish exists then update it. If not notify the 
        manager that the dish is not in the menu.
        """
        if name in self.menu_names:
            ind = self.menu_names.index(name)
            self.menu[ind]={'name':name,
                            'price':price,
                            'spice_lavel': spice,
                            'glute_index': gluten}
        else:
            print(f'Meal {name} not in the menu.')
        
    def remove_item(self, name):
        """ This method should check if the dish 
        is in the menu, if the dish exists then delete 
        it and print the updated dictionary. 
        If not notify the manager that the dish is 
        not in the menu."""
        if name in self.menu_names:
            ind = self.menu_names.index(name)
            self.menu_names.pop(ind)
            self.menu.pop(ind)
            print(self.menu)
        else:
            print(f'Meal {name} not in the menu.')


menu_list = [
        {'name':'Soup',
         'price':10,
         'spice_lavel': 'A',
         'glute_index': True},
        {'name':'Salad',
         'price':18,
         'spice_lavel': 'A',
         'glute_index': False},
        {'name':'French Fries',
         'price':5,
         'spice_lavel': 'C',
         'glute_index': False},
        {'name':'Beef bourguignon',
         'price':25,
         'spice_lavel': 'B',
         'glute_index': True},
        ]

menu_man = MenuManager(menu_list)
print(menu_man.menu)
print(menu_man.menu_names)

menu_man.add_item('pizza',20,'A',True)
menu_man.update_item('pizza',25,'B',False)
menu_man.remove_item('pizza')
