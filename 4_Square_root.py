# Solution-1 (Using Exponential Operator)
num = 64
num1 = int(input("Enter a number : "))

sr = num **(1/2)
sr1 = num1**(1/2)

print("The square root of ",num,"is ",sr)
print("The square root of ",num1,"is ",sr1)

# Solution-2 (Math module)
import math

num1 = int(input("Enter a number : "))

sr1 = math.sqrt(num1)

print("The square root of ",num1,"is ",sr1)

