# Soluiton-1
dict_1 = {1:2,3:4}
dict_2 = {5:6,7:8}

print(dict_1 | dict_2)

# Solution-2
dict_1 = {1:2,3:4}
dict_2 = {5:6,7:8}

print({**dict_1,**dict_2})

# Solution-3
dict_1 = {1:2,3:4}
dict_2 = {5:6,7:8}

dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)