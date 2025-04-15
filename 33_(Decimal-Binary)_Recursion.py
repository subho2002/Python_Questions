def ConverBinary(a):
    if a>1:
        ConverBinary(a//2)
    print(a%2,end=",")

ConverBinary(15)