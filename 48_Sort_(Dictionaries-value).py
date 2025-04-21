Laptop = {1:"Acer",2:"Dell",3:"HP",4:"Asus"}

# Solution-1
sv = sorted(Laptop.items() , key = lambda a : a[1])

print(sv)

# Solution-2
v = sorted(Laptop.values())
print(v)