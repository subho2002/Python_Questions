num = int(input("Enter any number "))

if num == 1:
    print(num," is not a prime number ")
else:
    for i in range(2,num):
        if num%i == 0:
            print(num," is not prime number")
            break
    else:
        print(num," is a prime number ")