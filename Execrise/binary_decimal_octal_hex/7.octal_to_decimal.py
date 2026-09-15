
octal = input("Enter octal Number : ")
decimal = 0
pow = len(octal) - 1

for binary in octal:
    value = int(binary) * (8 ** pow)
    decimal += value
    print(f"{binary} * 8 ^ {pow} = {value}")
    pow -= 1

print(decimal) 