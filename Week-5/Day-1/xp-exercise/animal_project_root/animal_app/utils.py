import json

def read_data(file_path:str, key:str)->list[dict]:
    with open (file_path, 'r') as file:
        data = json.load(file)
    return data[key]

def read_instance (data:list[dict], id):
    for instance in data:
        if instance['id'] == id:
            return instance
    return None    

def read_animal_by_family(data:list[dict], family_id):
    animal_list = []
    for instance in data:
        if instance['family'] == family_id:
            animal_list.append(instance)
    return animal_list

    