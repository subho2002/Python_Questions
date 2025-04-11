# Solution-1
print("This numbers is divisible by 13")
for i in range(1,100):
    if i %13 == 0:
        print(i)

# Solution-2
list1 = [93,84,62,89,33,76,78]
result = list(filter(lambda n : n%13 == 0,list1))
print('the numbers divisible by 13 are',result)