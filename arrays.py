# It start's from cero 
names = ["juan","david","martinez","rojas"]

#To get the infomation from an index
print(names[1])

#To change the index of an array
names[1]="davidR10"
print(names[1])

#To get the length of an array
print(len(names))

#To get the dataType
print(type(names))

#To add data into an array at the end of it
print(names)
names.append("B-boy")
print(names)

#To remove elements from an array
print(names)
names.remove("B-boy")
print(names)

#To delete by index
print (names)
del names[1]
print (names)

#To know if an element is in the array using "in"
print("juan" in names)

names.append("Santiago")
names.append("Jorge")
names.append("ray")
print(names)

print("Welcome to the party",names[0:3])
print("Welcome to the party",names[:3])
print("We are sorry, see you next weekend", names[3:5])
print("We are sorry, see you next weekend", names[3:])

print(f"The people who registered were:")
for i, name in enumerate (names):
    print(f"{name} with the index {i}")





















