value = input("Enter Your Prompt : ")

ans = ""

for i in value:

    # You hand ord() a single text character, and it hands you back the secret integer assigned to it.
    # ord("A") gives you 65
    # ord("a") gives you 97 (Uppercase and lowercase have different numbers!)
    # ord(" ") gives you 32 (Even the spacebar is a number)
    number_value = ord(i)

    # If we do bin(65), it outputs the string: "0b1000001"
    # The Problem: Notice that "0b" at the front? Python always attaches "0b" to the start of binary strings to tell other programmers, "Hey, this is a binary sequence, not the number one-million!" But we are building a clean text encoder, and we don't want those ugly "0b"s cluttering up our final answer.
    # Part B: The [2:] Slicer
    # In Python, you can slice a string apart using brackets and a colon. Computers start counting at 0. So, in the string "0b1000001":
    # Position 0 is "0"
    # Position 1 is "b"
    # Position 2 is "1"
    # When we attach [2:] to the end of a string, we are telling Python: "Start at position 2, and give me everything until the end of the string. Throw away positions 0 and 1."
    binary_value = bin(number_value)[2:]

    # increment of ans 
    ans =ans + binary_value + " "

print("Your Binary Output : ", end = "")
print(ans)

# a = bin(46)[:3]
# print(a)
