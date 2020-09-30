from random import randint

num1 = randint(2,12)
num2 = randint(2,12)

while True:
    answer = int(input(f"What is {num1} x {num2}? "))
    if answer != num1*num2:
        print("Incorrect - try again.")
    else:
        print("Correct!")
        break
