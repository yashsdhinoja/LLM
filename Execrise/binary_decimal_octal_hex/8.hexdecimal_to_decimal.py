hexdecimal = input("Enter HexDecimal Number :").upper()
hexdec_dictory = {
'0': 0,
'1': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'A': 10,
'B': 11,
'C': 12,
'D': 13,
'E': 14,
'F': 15
}

ans  = 0
pos = 0

for character in hexdecimal[::-1]:
    value = hexdec_dictory[character]
    ans += value * (16 ** pos)
    pos += 1

print(ans)
