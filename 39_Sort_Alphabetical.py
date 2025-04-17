string = "Harry Potter and the Goblet of Fire"

w = string.split(' ')

print(w)

# Convert each word to lowercase
for i in range(len(w)):
    w[i] = w[i].lower()

print(w)

# Sort the list
w.sort()
print(w)

# Print each word
for i in w:
    print(i)
