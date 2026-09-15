cars = ["Tata","Maruti Suzuki","Hyundai","Mahindra","Kia","Toyota","Honda","Ford","Nissan"]
# print(type(cars))

i = 0
for d in cars:
    if d == "Tata":
        continue
    print(d, i)
    i = i + 1