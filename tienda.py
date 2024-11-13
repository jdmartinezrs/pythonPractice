print("*****************************************")
print("***          WELCOME TO THE           ***")
print("***            PET'S SHOP             ***")
print("*****************************************")
print("")
num_dogs = 10
num_cats = 19
num_birds = 7
total_animals = num_dogs + num_cats + num_birds

print('Please insert your name')
name = input()
print ("Please insert your lastname")
last_name = input()

#Concatenation
full_name = name + " " + last_name

print('thanks for visit us', full_name)

while True:
    print("")
    print("====================================")
    print("Select the option you prefer")
    print("1: To know how many animals we have")
    print("2. To buy a animal")
    print("3. Exit")
    print("====================================")
    print("")
    respuesta = int(input())

    if respuesta == 1:
        print ("Currently we have:")
        print ( num_dogs, "dogs", num_cats, "cats", num_birds,"birds")
        print ("We have in total ",total_animals,"animals")
    elif respuesta == 2:
        print("Wich animal do you want to buy")
        animal = input()
        article = "an" if animal[0].lower() in "aeiou" else "a"
        print(f"You have bought {article} {animal}")
    elif respuesta == 3:
        break
print('You have left the application')
    















