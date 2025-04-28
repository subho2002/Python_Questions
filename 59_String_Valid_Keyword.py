import keyword

words = ['bun','break','corn','continue','lambda','global','pending']

for i in range(len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],'is a keyword in python')
    else:
        print(words[i],'is not a keyword in python')
