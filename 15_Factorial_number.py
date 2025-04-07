# Solution-1
# num = int(input("Enter any number "))

# fact = 1

# if num < 0:
#     print(num," don't have any factorial ")
# if num == 0:
#     print(num," 's factorial is 0 ")
# if num > 0:
#     for i in range(1,num+1):
#         fact = fact*i
# print(num,"'s factorial number is ",fact)

# Solution-2

def factorial_num(x):
    if x == 0:
        return 1
    else:
        return x * factorial_num(x-1)
    
num1 = int(input("Enter any number "))

result = factorial_num(num1)

print(num1,"'s factorial number is ",result)
