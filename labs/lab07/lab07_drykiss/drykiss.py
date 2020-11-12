import operator
from functools import reduce

def product(my_list):
    return  reduce(operator.mul, my_list, 1)

def get_list():
    letters = ['a', 'b', 'c', 'd', 'e']
    my_list = [int(input(f"Enter {letters[i]}: ")) for i in range(len(letters))]
    return my_list

if __name__ == '__main__':
    my_list = get_list()
    print("Minimum: " + str(min(my_list)))
    print(f"Product of first 4 numbers:\n  {product(my_list[:4])}")
    print(f"Product of last 4 numbers:\n  {product(my_list[1:])}")