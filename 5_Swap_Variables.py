# Solution-1 (Using Third Variable)
x = 10
y = 11

print("X= ",x)
print("Y= ",y)

z = x
x = y 
y = z

print("X= ",x)
print("Y= ",y)

# Solution-2 (Without using Third Variable)
x1 = 12
y1 = 13

print("X= ",x1)
print("Y= ",y1) 

x1,y1 = y1,x1

print("X= ",x1)
print("Y= ",y1)

# Solution-3 (With Arithmetic Operator)
x2 = 14
y2 = 15

print("X= ",x2)
print("Y= ",y2) 

x2 = x2+y2
y2 = x2-y2
x2 = x2-y2

print("X= ",x2)
print("Y= ",y2) 