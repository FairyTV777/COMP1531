def guess(low, high):
    mid = (low+high) // 2
    print("My guess is: " + str(mid))
    print("Is my guess too low (L), too high (H), or correct (C)?")
    answer = input()
    if answer == 'C':
        print("Got it!")
    elif answer == 'H':
        guess(low, mid)
    elif answer == 'L':
        guess(mid, high)

if __name__ == '__main__':
    print("Pick a number between 1 and 100 (inclusive)")
    guess(1, 100)