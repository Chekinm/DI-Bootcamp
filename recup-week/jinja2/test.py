from jinja2 import Template, filters
from jinja2.filters import escape
import jinja2
""" lesson 1"""


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

# per = Person('MIke',28)
# per2 = {'name':'fedya','age':56}
# tm = Template("hi {{p.name}}, you are {{p.age * 1.5}}")
# msg = tm.render(p=per)
# msg2 = tm.render(p=per2)
# print(msg, msg2, sep='\n')

""" lesson 2"""

# raw_string = """this is link <a href=www.google.com'>GOOGLE</a>"""
# filtered_string = escape(raw_string)
# tm1 =Template("This string is not prepared (will see link) {{ st }}")
# tm2 =Template("This string is filtered with e flag {{ st|e }}")
# tm3 = Template("This one use filtered string {{f_st}}")

# msg1 = tm1.render(st=raw_string)
# msg2 = tm2.render(st=raw_string)
# msg3 = tm3.render(f_st=filtered_string)
# msg4 = filtered_string


# with open('res.htm', 'w') as f:
#     f.writelines((msg1,msg2,msg3,msg4))
# print(msg1, msg2,msg3,msg4)

""" lesson 3"""

# cities = [{'id':1,'name':'TelAvive'},
#           {'id':2,'name':'Rishon'},
#           {'id':3,'name':'Heifa'},
#           {'id':4,'name':'Ashdod'},
#           ]

# link = """<select name="cities">
# {%-for city in cities %}
# {%- if city.id > 2 %}
#     <option value={{city.id}}>{{city.name}}</option>
# {%- elif 1< city.id < 3%}
#     <option value=elif>elif</option>
# {%- else %}
#     <option value=else>else</option>


# {%- endif %}
# {%-endfor %}
# </select>"""

# tm = Template(link)
# msg = tm.render(cities=cities)

# with open('res.htm', 'w') as f:
#     f.write(msg)
# print(msg)

"""lesson 4"""

# car = [
#     {'mod':'a', 'pr':1000},
#     {'mod':'b', 'pr':2000},
#     {'mod':'c', 'pr':3000},
# ]
# tmpl_body = """
# {%- for car in obj -%}
#     {% filter upper %} {{car.mod}} {% endfilter%} - price - {{car.price}} 
# {% endfor %}
# """
# tm = Template(tmpl_body)
# msg = tm.render(obj=car)
# print(msg)

"""lesson5"""

# car = [
#     {'mod':'a', 'pr':1000, 'color': 'black'},
#     {'mod':'b', 'pr':2000, 'color': 'red'},
#     {'mod':'c', 'pr':3000, 'color': 'green'},
# ]

# tmpl_body = """
# {%- macro str_car(car_dict) -%}
#     <ul>
#         {%- for key, value in car_dict.items() %}
#             <li>{{-key}} - {{value-}}</li>
#         {%- endfor %}
#         </ul>  
# {%- endmacro -%}

# <ol>
# {%- for car_inst in car_list %}
#     <li><strong>{{ car_inst.mod }}</strong>
#         {{ str_car(car_inst) }}
#     </li>
# {%- endfor -%}
# </ol>

# """


# tm = Template(tmpl_body)
# msg = tm.render(car_list=car)

# with open('res.htm', 'w') as f:
#     f.write(msg)
# print(msg)

# """lesson 5.1"""

# car = [
#     {'model':'volvo', 'pr':1000, 'color': 'black'},
#     {'model':'bmw', 'pr':2000, 'color': 'red'},
#     {'model':'subaru', 'pr':3000, 'color': 'green'},
# ]


# from jinja2 import Environment, FileSystemLoader

# env = Environment(loader=FileSystemLoader('C:/Prog/DI-Bootcamp/recup-week/jinja2'))
# tm = env.get_template('test1.html')

# msg = tm.render(context_variable_from_render=car)

# with open('res.htm', 'w') as f:
#     f.write(msg)
# print(msg)

# a = {'a':[{'b':1},{'c':2}]}

# for item in a['a']:
    
#     if 'b' in item:
#         print(item)
#         a['a'].pop(item)


a = [1,8,6,2,5,4,8,3,7]
b = list(enumerate(a))
c = sorted(b, key=lambda x: x[1], reverse= True)
print(c)
d = sorted(list(filter(lambda x: x[0] <= c[0][0] or x[0]>=c[1][0], c)),key=lambda x: x[0])
print(d)

a6 =[int(x>=8) for x in a]
print(a6)
