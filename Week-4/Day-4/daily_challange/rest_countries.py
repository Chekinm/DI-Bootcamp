import requests
import json
from dataclasses import dataclass
from random import sample

@dataclass
class Country():
    
    name: str
    capital: str
    flag_url: str        
    subregion: str     
    population: int

def get_random_country_list_from_api(num):
    response = requests.get('https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population')
    if response.status_code == 200:
        countries_list = json.loads(response.content)
    else:
        print('response code: '+ response.status_code)
        return None
    
    return sample(countries_list, k=num)

def get_info_for_countries(countries:list)->list[Country]:
    country_list = []
    for country in countries:
        try:
            name = country['name']['common'],
        except KeyError:
            name = None
        try:
            capital = country['capital'][0],
        except ( IndexError, KeyError):
            capital = None
        try:
            flag = country['flags']['png'],
        except KeyError:
            capital = None
        try:
            subregion = country['subregion'],
        except KeyError:
            capital = None
        try:
            population = country['population']
        except KeyError:
            capital = None
        country_list.append(Country(name,capital,flag,subregion,population))
    return country_list