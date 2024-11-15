from datetime import datetime


print("*****************************************")
print("***          WELCOME TO THE           ***")
print("***            PET'S SHOP             ***")
print("*****************************************")
print("")

#Inventory

inventory= {"dogs": 10, "cats": 7, "birds": 7}

total_animals = 0
for val in inventory.values():
    total_animals += val
print(f"Currently we have{total_animals} in our store")



print('Please insert your name')
name = input()
print ("Please insert your lastname")
last_name = input()

#Concatenation
full_name = name + " " + last_name

print('thanks for visit us', full_name)


compras = []
def show_menu():
    print("")
    print("====================================")
    print("Select the option you prefer")
    print("1: To know how many animals we have")
    print("2. To buy a animal")
    print("3. To show the purshases done")
    print("4. Exit ")
    print("")
    print("====================================")
    

def show_inventory():
        print ("*******   INVENTORY   *******")
        for key, value in inventory.items():
            print(f"  {key}:{value}")       
        print (f"Currently we have {total_animals} animals in our store")
        print("")


def buy_an_animal():
    shopping_cart = []
    while True:
        print("Write 'f' to finish the array, or 'v' to see your cart")
        print("Which animal would you like to buy? Note that purchases are limited to one per species.")
        animal = input().strip()

        if animal == "f":
            break
        elif animal == "v":
            print(f"Your shopping cart has: {shopping_cart}")
            continue
        if animal not in inventory:
            print(f"We dont have {animal} at this time")

        elif inventory[animal]== 0:
            print(f"we are sorry, we have just left the last {animal}")
        elif animal not in shopping_cart:
            shopping_cart.append(animal)

        else:
            print("You’ve already added this animal to your cart.")

    print("The content of your cart is:")
    for animal in shopping_cart:
        print("  ", animal)
        inventory[animal] -= 1

    date = datetime.now()
    compras.append((name, shopping_cart, date))

def show_purchases():
    print("")
    print("**** Purchases made ****")
    for purshase in compras:
        print(f"   {purshase[0]} compró{purshase[1]} en {purshase[2]}")
while True:
    show_menu()
    respuesta = int(input())
    if respuesta == 1:
         show_inventory()    
    elif respuesta == 2:
         buy_an_animal()
    elif respuesta == 3:
        show_purchases()
    elif respuesta == 4:
        break

print('You have left the application')


















