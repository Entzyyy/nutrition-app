def fibonacci(n): # iterative version
    while n != 0 and n != 1:
    (a, b) = (b, a % b)
    return b