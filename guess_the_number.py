import random

def guess():

    randomNumber= random.randint(1, 21)
    count= 0

    while True:
        count += 1
        number= int(input("Enter a number between 1 and 20"))

        if number < randomNumber:
            print("Too small")

        elif number > randomNumber:
            print("Too Large")

        else:
            print("You have got it in", count, "tries")
            break

if __name__ == "__main__":
    guess() 