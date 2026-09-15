def addd(u):
    # lambda arguments : expression     
    return lambda d:d + u

addfunction = addd(9)
print(f"===========================================")
ui = int(input("Enter Number to Add : "))
result = addfunction(ui)
print(f"Result = {result}")
print(f"===========================================")

def leess(y):
    # lambda arguments : expression     
    return lambda b:b - y

leess_func = leess(3)
print(f"===========================================")
ui2 = int(input("Enter Number to Less : "))
result = leess_func(ui2)
print(f"Result = {result}")
print(f"===========================================")


def div(i):
    # lambda arguments : expression     
    return lambda j:j / i

divfunction = div(3)
print(f"===========================================")
ui3 = int(input("Enter Number to Divide : "))
result = divfunction(ui3)
print(f"Result = {result}")
print(f"===========================================")


def double(o):
    # lambda arguments : expression     
    return lambda k:k * o

doublefunction = double(5)
print(f"===========================================")
ui4 = int(input("Entre Number : "))
result = doublefunction(ui4)
print(f"Result : {result}")
print(f"===========================================")