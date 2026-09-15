def cum(number):
    if len(number) == 0:
        return 0 
    else:
        return number[0] + cum(number[1:])
    
my_list = list(map(int, input("Enter numbers separated by spaces: ")))
print("Sum = ",cum(my_list))
