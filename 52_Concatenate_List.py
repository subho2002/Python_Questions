# Solution-1
l1 = [1,2,3,5,'o','p','e']
l2 = [1,6,8,5,'o','f','r']

l3 = l1+l2
print(l3)

# Solution-2
l1 = [1,2,3,5,'o','p','e']
l2 = [1,6,8,5,'o','f','r']

l3 = list(set(l1+l2))
print(l3)

# Solution-3
l1 = [1,2,3,5,'o','p','e']
l2 = [1,6,8,5,'o','f','r']

l1.extend(l2)
print(l1)