s1 = {1,2,3,4,5}
s2 = {9,3,2,8,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.intersection_update(s2))

s3 = s1.symmetric_difference(s2)
print(s3)

print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

# s1.remove(4)
print(s1)
# s1.discard()
print(s1)

s4 = s2.pop()
print(s4)
del s2
s3.clear()

if 9 in s1:
    print("Present")
else :
    print("Absent")

s1.add(8)
# s3.append("Nine")