people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "hosue": "Ravenclaw"},
    {"name": "Draco", "house": "Slythering"}
]

#instead of using this method 
# def f(person):
#     return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)