import sys

def valid(square, n):
    valid = True

    if len(square) != n:
        valid = False

    for row in square:
        if len(row) != n:
            valid = False

    nums = []
    for row in square:
        for num in row:
            nums.append(num)

    if len(nums) != len(set(nums)):
        valid = False

    if n < 3:
        valid = False

    return valid

def horizontal(square, _sum):
    for row in square[1:]:
        if sum(row) != _sum:
            return False

    return True

def vertical(square, _sum, n):
    i = 0
    while i < n:
        col = [row[i] for row in square]
        if sum(col) != _sum:
            return False
        i += 1

    return True

def diagonal(square, _sum, n):
    diagonalSum = 0
    i = 0
    while i < n:
        diagonalSum += square[i][i]
        i += 1

    if diagonalSum != _sum:
        return False

    diagonalSum = 0
    i = 0
    while i < n:
        diagonalSum += square[i][n-1-i]
        i += 1

    if diagonalSum != _sum:
        return False

    return True


if __name__ == '__main__':
    n = int(input())
    square = []
    for i in range(0,n):
        square.append([int(num) for num in input().split()])

    _sum = sum(square[0])

    if valid(square, n) == False:
        result = 'Invalid data: missing or repeated number'
    else:
        if horizontal(square, _sum) and vertical(square, _sum, n) and diagonal(square, _sum, n):
            result = 'Magic square'
        else:
            result = 'Not a magic square'

    print(result)