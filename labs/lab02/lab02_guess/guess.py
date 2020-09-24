print("Pick a number between 1 and 100 (inclusive)")
print("My guess is: 50")

higher_bound = None
lower_bound = None

print("Is my guess too low (L), too high (H), or correct (C)?")
answer = input()
if answer == 'L':
    lower_bound = 50
    higher_bound = 100
    print("My guess is: " + str(75))

    while True:
        print("Is my guess too low (L), too high (H), or correct (C)?")
        answer = input()
        if answer == 'L':
            lower_bound = (lower_bound + higher_bound) // 2
            print("My guess is: " + str((lower_bound + higher_bound) // 2))
        elif answer == 'H':
            higher_bound = (lower_bound + higher_bound) // 2
            print("My guess is: " + str((lower_bound + higher_bound) // 2))
        elif answer == 'C':
            break

elif answer == 'H':
    lower_bound = 1
    higher_bound = 50
    print("My guess is: " + str(25))

    while True:
        print("Is my guess too low (L), too high (H), or correct (C)?")
        answer = input()
        if answer == 'L':
            lower_bound = (lower_bound + higher_bound) // 2
            print("My guess is: " + str((lower_bound + higher_bound) // 2))
        elif answer == 'H':
            higher_bound = (lower_bound + higher_bound) // 2
            print("My guess is: " + str((lower_bound + higher_bound) // 2))
        elif answer == 'C':
            break

print("Got it!")