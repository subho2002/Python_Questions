a = [[1,2,3],
     [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        T[j][i] = a[i][j]

for r in T:
    print(r)
