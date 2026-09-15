superhero = ["Iron Man","Spider Man","Captain America","ThorHulk","Black Widow","Wolverine","Black Panther","Doctor Strange"]

# Exit the loop when x is "banana"
for y in superhero:
    print(y)
    if y == "Black Panther":
        break

print("")

# Exit the loop when x is "banana", but this time the break comes before the print:
for x in superhero:
    if x == "Black Panther":
        break
    print(x)