def sum_natural(n):
    if n <= 1 :
        return n 
    else:
        return n + sum_natural(n-1)
    
num = int(input("Enter any number "))
sum = sum_natural(num)
print(sum)