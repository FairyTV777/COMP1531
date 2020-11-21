def generate(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n >= 2:
        i = 2
        fibonacci = [0, 1]
        while i < n:
            fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
            i += 1
        return fibonacci