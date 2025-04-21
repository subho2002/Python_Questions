string = input("Enter any string you want ")

try :
    num = int(input("Enter any number you want "))
    print(string+num)
except(ValueError,TypeError) as b:
    print(b)
    print("thank you ")