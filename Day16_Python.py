v = int(input("Enter any number you want "))
match v:
    case 0 :
        print("It is Zero")
    case 999:
        print("This is a special number ")
    case _ if v %2 ==0 :
        print(v," is a even number  ")
    case _ if v % 2 != 0 :
        print(v," is a Odd number  ")
    case _ :
        print(v," is your number ")


