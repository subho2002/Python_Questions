upper = int(input("Enter upper number: "))
lower = int(input("Enter lower number: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    total_sum = 0  # Renamed sum to total_sum
    temp = num

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** order
        temp = temp // 10

    if num == total_sum:
        print(num)
