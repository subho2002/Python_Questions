dic1 = {
    'name' : 'Person',
    'age' : 24,
    'work' : 'Kuch vi',
    'place' : 'Hydrabad'
}

dic2 = {
    'name' : 'Person2',
    'age' : 25,
    'work' : 'Kuch vi2',
    'place' : 'Hydrabad3'
}

dic1.update(dic2)
print(dic1)

# d = dic1.pop()
# print(d)

d = dic1.popitem()
print(d)

del dic2
del dic1['age']

dic1.update({'time':'8 hrs'})