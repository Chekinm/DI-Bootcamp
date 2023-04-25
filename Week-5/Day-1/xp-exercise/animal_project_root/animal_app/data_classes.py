import json

class Animals():

    def __init__(self, file_path:str):
        self.list = []
        self.key = 'animals'
        with open (file_path, 'r') as file:
            data = json.load(file)
        self.list = data[self.key]
    
class Animal():
    
    def __init__(self,  animals:Animals, id):
        self.data = {}
        self.id = id
        
        for animal in animals.list:
            if animal['id'] == self.id:
                self.data = animal
        if not self.data:
            self.data['name'] = 'id_error check json file'



class Families():

    def __init__(self, file_path:str):
        self.list = []
        self.key = 'families'
        with open (file_path, 'r') as file:
            data = json.load(file)
        self.list = data[self.key]
    
class Family():
    
    def __init__(self,  families:Families, id):
        self.data = {}
        self.id = id
        self.animals_list = []
        for family in families.list:
            if family['id'] == self.id:
                self.data = family
        if not self.data:
            self.data['name'] = 'id_error check json file'


    def get_family_memebers (self, animals:Animals):
        self.animals_list = []   
        for animal in animals.list:
            if animal['family'] == self.id:
                self.animals_list.append(animal)
        

    