class Person():
    
    def __init__(self) -> None:
        user_input = input().split(',')
        self.name = user_input [0]
        self.age = int(user_input[1])
        self.score = int(user_input[2])
    
    def __repr__(self):
        return repr((self.name, self.age, self.score))
    
class Grope_of_person (list):

    def sort_by_name(self):
        self.sort(key=lambda person: person.name)
    def sort_by_age(self):
        self.sort(key=lambda person: person.age)
    def sort_by_score(self):
        self.sort(key=lambda person: person.score)
    
persons = Grope_of_person()

print(type(persons))
for _ in range(5):
    person = Person()
    persons.append(person)

persons.sort_by_score()
persons.sort_by_age()
persons.sort_by_name()

print(persons)



    