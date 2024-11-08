print("*****************************************")
print("***          WELCOME TO THE           ***")
print("***            PET'S SHOP             ***")
print("*****************************************")

num_dogs = 10
num_cats = 19
num_birds = 7
total_animals = num_dogs + num_cats + num_birds

print('Please insert your name')
name = input()
print ("Por favor escribe tu apellido")
last_name = input()

#Concatenation
full_name = name + " " + last_name

print('thanks for visit us', full_name)
print ("Currently we have:")
print ( num_dogs, "dogs", num_cats, "cats", num_birds,"birds")
print ("We have in total ",total_animals,"animals")







