def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

fib = int(input("Enter any number "))
if fib <= 0 :
    print("Enter a positive number")
else:
    print("Fibonacci sequence ")
    for i in range(fib):
        print(fibonacci(i))