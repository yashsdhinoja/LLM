def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return f"Yes, {index} is Found in the List."
    return f"No, {index} is Found in the List."

my_list = [12, 42, 90, 56, 34, 23]

print(linear_search(my_list, 34))
print(linear_search(my_list, 89))