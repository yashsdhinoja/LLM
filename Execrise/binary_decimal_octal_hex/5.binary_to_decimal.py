binary = input("Enter binary Number : ")
decimal = 0
power = len(binary) - 1

for digit in binary:
    value = int(digit) * (2 ** power)
    decimal += value
    print(f"{digit} * 2 ^ {power} = {value}")
    power -= 1

print(decimal) 


