color_do = {"black", "white", "red", "blue", "yellow", "green", "orange", "pink", "purple", "brown"}
j = list(color_do)

i = 0
while True:
    print(f"Do While loop : {i}, {j[i]} ")
    i += 1

    if i >= len(j):
        break
