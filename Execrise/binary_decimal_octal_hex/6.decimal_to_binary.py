decimal = int(input("Enter decimal number :"))
ans = ""

if decimal == 0:
    ans = 0

else:
    while decimal > 0:
        bit = decimal % 2
        ans = str(bit) + ans
        decimal = decimal // 2

    print(ans)
