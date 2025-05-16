eid = [1001,1002,1003,1004,1005,1006,1007,1008]

print(eid)
print(eid[1:9])
print(eid[:9])
print(eid[1:])
print(eid[3:8])
print(eid[3:8:2])
print(eid[-8:-3])

for i in eid:
    print(i)

if 1004 in eid:
    print("1004 is present")
else:
    print("1004 is not present")
