def factorial(n):
    if n ==1 or n==0 :
        return 1
    return n * factorial(n-1)

print(factorial(6))

def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(6))