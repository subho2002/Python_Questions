def factorial_num(a):
    if a < 1 :
        return 1
    else :
        return a * factorial_num(a-1)
    

num = int(input("Enter any number "))
fact = factorial_num(num)

print(fact)