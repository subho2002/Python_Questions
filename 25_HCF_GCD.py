def HCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if ((x%i == 0 )and(y%i == 0)):
            hcf = i
    return hcf

a = 12
b = 30

print("HCF of ",a,"and ",b,"is : ",(HCF(a,b)))
