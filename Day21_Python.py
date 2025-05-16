def average(a = 8 , b = 12):
    return (a+b)/2


avr = average(5,8)
print("Average is ",avr)

def ave_rage(*num):
    sum = 0 
    for i in num:
        sum = sum +i
    print("Average2 is ",sum/len(num))

avr2 = ave_rage(5,8)

def names(**name):
    print("Name ",name['fname'],name['lname'])

names(fname = "Dark" ,lname = "Rider")