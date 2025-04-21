Laptop = {1:"Acer",2:"Dell",3:"HP",4:"Asus"}

print(Laptop)

# Solution-1
for key,value in Laptop.items():
    print(key,"-",value)

# Solution-2
for key in Laptop:
    print(key,":",Laptop[key])