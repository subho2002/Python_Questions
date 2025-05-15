i = int(input("Enter any number you want "))
try:
    while  i <= 8 :
        i = int(input("Enter any number you want "))
        print(i)
    else:
        print("Done with trhe Loop")
except (ValueError) as f:
    print(f)