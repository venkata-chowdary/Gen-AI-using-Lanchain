from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    

new_person: Person = {'name': "Chowdary", 'age': 22}
print(type(new_person['age']))