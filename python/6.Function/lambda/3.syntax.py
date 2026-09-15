# number = input("Enter 5 Numbers : ")
# while len(number) < 5:
#     print("Too Short Number")    
#     number = input("Enter 5 Numbers : ")
# if len(number) == 5:
#     doubled = list(map(lambda x:int(x) * 2, number))    
#     print(f"Double Digit : {doubled}")
# else:
#     print("Length is Tooo Big !!!")
#     number = input("Enter 5 Numbers : ")

numbers = input("Enter 10 Number : ")

while len(numbers) < 10:
	print("Too Short Number")    
	numbers = input("Enter 10 Number : ")

if len(numbers) == 10:
    numbers = list(filter(lambda x:int(x) % 2 == 0, numbers))
    # numbers = list(filter(lambda x:int(x) % 2 != 0, numbers))
    print(numbers)
else:
	print("Noo !!!")