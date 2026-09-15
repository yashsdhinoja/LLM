# A do-while loop executes the body at least once before checking the condition. In Python, 
# this is written using while True: and placing an if condition with a break at the bottom.

number = [10, 20, 30, 40, 50]
i = 0

while True:
    print(f" {i} : A Do-While Loop Index : {number}")
    i += 1

    if i >= len(number):
        break