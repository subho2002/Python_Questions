l = [1,2,3,1,4,1,5,1,6,1,7,1,8]

print(l)
l.append(1)
print(l)
l.sort() #reverse = True
print(l)
print(l.count(1))
print(l.index(5))
m = l.copy()
m[0] = 0
l.insert(4,12)
l.extend(m)
print(l)