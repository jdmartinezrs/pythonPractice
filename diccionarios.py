#list  with key and value

person = {"name": "davidR10", 
          "age": 29,
          "lastname": "Martínez"}

#To update the value of a key
person["name"] = "DavidRojas"

#To add a field
person["nickname"]="Gobernador"
print(person)

person["name"] ="BBOY"
person["rol"]= "creator"

person["nickname"]="Diomedes"
person["rol"]="Desenvolvedor"

print(person)
#To see only the keys in the dictionary
print(person.keys())

#To see the dictionary values
print(person.values())

#To show all the dicctionay
print(person.items())

# To show all the keys
for key in person.keys():
    print (key)
# To show all the values
for value in person.values():
    print(value)

# It shows a tuplas list
for item in person.items():
    print(item)

# It returns a tuplas lits with each key and value
for key,value in person.items():
    print(f"the key {key} has the value {value}")

# To make some validations
print("nickname" in person)
print("knsdfvkl" in person)

