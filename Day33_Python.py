dic = {
    'name' : 'Person',
    'age' : 24,
    'work' : 'Kuch vi',
    'place' : 'Hydrabad'
}

print(dic['work'])
print(dic.get(56))
print(dic.keys())
print(dic.values())
 
for i in dic:
    print(i,'-',dic[i])

for key in dic:
    print(key)

for val in dic:
    print(dic[val])