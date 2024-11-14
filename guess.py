import random

def roll_a_dice():
    return random.randint(2,12)

def ask_for_answer():
    print("Insert your prediction")
    print("1. Even number")
    print("2. Odd number")
    print("3. End the game")
    return int(input())


def print_result(number,prediction):
    is_even = number % 2 == 0
    if is_even and prediction == 1:
        print("You win!, number of dice:",number)
    elif not is_even and prediction == 2:
        print("You win!, number of dice:",number)
    else:
        print("You loose, the numbes was",number)


while True:
    number = roll_a_dice()
    prediction = ask_for_answer()
    if prediction == 3:
        break
    print_result(number, prediction)
print("Thanks for playing")




