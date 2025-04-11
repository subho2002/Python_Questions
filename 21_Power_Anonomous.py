num = int(input("Enter any number "))

# Create a list with 2 raised to the power of each number from 0 to num
result = list(map(lambda a: 2 ** a, range(num)))

print(result)

# Loop through the range num to print the result for each power
for i in range(num):
    print("The value of 2 raised to the power", i, "is", result[i])
