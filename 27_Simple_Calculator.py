print("-----This is my simple Calculator-----")

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplition \nPress 4 for division")

choice = int(input("enter you choice form 1-4 "))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)