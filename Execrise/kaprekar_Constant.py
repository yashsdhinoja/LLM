raw_input = input("Enter numbers separated by spaces (e.g., 5 7 3 9): ")

numbers = [int(x) for x in raw_input.split()]

n = len(numbers)

asc_list = numbers[:]  
for i in range(n):
    for j in range(n - i - 1):
        
        if asc_list[j] > asc_list[j + 1]:
            asc_list[j], asc_list[j + 1] = asc_list[j + 1], asc_list[j]

desc_list = numbers[:]  
for i in range(n):
    for j in range(n - i - 1):

        if desc_list[j] < desc_list[j + 1]:
            desc_list[j], desc_list[j + 1] = desc_list[j + 1], desc_list[j]

print("\nResults:")
print("Ascending: ", asc_list)
print("Descending:", desc_list)

d_list = int("".join(map(str, desc_list)))
a_list = int("".join(map(str, asc_list)))

less = d_list - a_list
count = 6174
while count != less:
    print("Match Total = ", less)
    count += 2
    break
