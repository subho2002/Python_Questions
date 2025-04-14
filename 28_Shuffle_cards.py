import random ,itertools

deck = list(itertools.product(range(1,14),["Spade","club","Hearts","Diamond"]))

random.shuffle(deck)

for i in range(4):
    print(deck[i][0],"of",deck[i][1])
